# LogAnalysis
### Udacity Full Stack Web Developer Nanodegree Project

#### A Python script that provide internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

#### Requirement
1. Python 3.6
2. Udacity Full Stack Nanodegree VM with built in PostgreSQL installed

#### Installation
1. Set up and run the vagrant virtual machine from https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0
2. Copy the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
3. Put the extracted file into the vagrant directory, which is shared with your virtual machine.
4. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql
5. Copy the files inside this folder into the vagrant directory
6. Run python3 log_analysis.py