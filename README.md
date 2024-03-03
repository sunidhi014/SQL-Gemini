# SQL Gemini App
SQL Gemini App is a Streamlit application designed to convert English queries into SQL commands for interacting with a sales database. 
Users can input their questions in English, and the app translates them into SQL queries, fetching the corresponding data from the database.

## Getting Started
To get started with SQL Gemini App, follow the instructions below.
#### Install Dependencies
```bash
pip install -r requirements.txt
```
#### Run the Streamlit App
```bash
streamlit run main.py
```

## Customization
#### Download a Dataset from Kaggle
Visit [Kaggle](https://www.kaggle.com/) and download a dataset of your choice in CSV format. Save the CSV file in the project directory.
#### Generate SQLite Table
Run the sqlite.py script to generate an SQLite table from your CSV file. Replace my csv file with the name of your downloaded CSV file, 
and my table name with your desired table name.
#### Customize SQL Queries
Modify the main.py file to customize SQL queries as required. Update the prompt variable with your desired prompt for the Streamlit app.
```bash
prompt = """
Your customized SQL prompt goes here.
"""
```
