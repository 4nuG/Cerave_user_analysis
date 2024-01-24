# Cerave User Analysis

## Project pipeline

First do analysis on a small set of data then automate the process: 
- beautifulsoup/selinium csv or twscrape
- Wrangle and clean data using jmp vs tableau
- Exploratory data analysis
- Place cleaned data in aws s3 bucket
- Access bucket using python and begin analysis
  User race
  User age
  User gender
- Build graphs to visualize data

Automation:
- From Twitter (external data source), scrape data (semi-structured data -> JSON format by default maybe transforme to parquet?) using python script on AWS EC2.
The python script will upload raw data (bronze data) to AWS S3 everyday (24 hr)
- (OPTIONAL) Initial data validation using Pydantic to generate cleaned data (silver data). THEN S3 bucket will have a trigger that calls a lambda function every time a parquet data file is inserted into a specified folder. The lambda is only called when both conditions are true (Folder and parquet file type). This lambda function reads the new file from aws s3 bucket, does data processing/analyzing (attaches sentiment), and writes it back to another S3 bucket (different from original one) (silver data). 
- Load AWS Redshift (do dbt transformations and dbt tests) and/or AWS Athena for querying 
- Load AWS RDS (postgres) –for future projects
- Generate dashboard on Metabase to display findings from the data (Visual aspect of project)


