#!/usr/bin/python3
# "Database code" for the Log Analysis Newspaper DB.

import psycopg2

DBNAME = "news"


def get_most_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select
            title, count(*) as num
        from
            articles
        join
            log
        on
            ('/article/' || articles.slug) = log.path
        group by
            title
        order by
            num desc;
    """)
    return c.fetchall()
    db.close()


def get_most_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select
            name, num
        from
            (select
                author, count(*) as num
            from
                articles
            join
                log
            on
                ('/article/' || articles.slug) = log.path
            group by
                author
            order by
                num desc) as author_views
        join
            authors
        on
            authors.id = author_views.author
        order by
            num desc;
    """)
    return c.fetchall()
    db.close()


def get_day_most_error():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select
            date(time) as log_date,
            round(((t2.num * 1.0) / count(*)) * 100, 1) as error_percentage
        from
            log
        join
            (
            select
                date(time) as log_date, count(*) as num
            from
                log
            where
                status = '404 NOT FOUND'
            group by
                log_date
            ) as t2
        on
            date(time) = t2.log_date
        group by
            date(time), t2.num
        having
            round(((t2.num * 1.0) / count(*)) * 100, 1) > 1
        order by
            date(time) asc
    """)
    return c.fetchall()
    db.close()

popular_articles = get_most_popular_articles()
print("Most Popular Articles by views according to web server log:")
for row in popular_articles:
    text = "\"{}\" - {} views".format(row[0], row[1])
    print(text)

print("\n")

popular_authors = get_most_popular_authors()
print("Most Popular Authors by article views according to web server log:")
for row in popular_authors:
    text = "\"{}\" - {} views".format(row[0], row[1])
    print(text)

print("\n")

most_errors_days = get_day_most_error()
print("Day with error status code percentage more than 1 %:")
for row in most_errors_days:
    text = "\"{}\" - {} % errors ".format(row[0], row[1])
    print(text)
