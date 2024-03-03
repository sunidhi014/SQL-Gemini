import sqlite3
import pandas as pd

# Connect to SQLite and create a database (e.g., "sales_database.db")
connection = sqlite3.connect("sales_database.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Read data from CSV using pandas
sales_data = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Create a table named "sales_table" and insert data
sales_data.to_sql("sales_table", connection, index=False, if_exists="replace")

# Commit the changes
connection.commit()

# Close the connection
connection.close()