import streamlit as st
import sqlite3
import google.generativeai as genai

## Configure Genai Key
genai.configure(api_key=GOOGLE_API_KEY)

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You specialize in converting English questions to SQL queries! The SQL database is named SALES_TABLE and contains the following columns - ORDERNUMBER, QUANTITYORDERED, PRICEEACH, ORDERLINENUMBER, SALES, ORDERDATE, STATUS, QTR_ID, MONTH_ID, YEAR_ID, PRODUCTLINE, MSRP, PRODUCTCODE, CUSTOMERNAME, PHONE, ADDRESSLINE1, ADDRESSLINE2, CITY, STATE, POSTALCODE, COUNTRY, TERRITORY, CONTACTLASTNAME, CONTACTFIRSTNAME, DEALSIZE.
    For example:
    Example 1 - How many entries of records are present?
    The SQL command will be something like this:
    SELECT COUNT(*) FROM SALES_TABLE;
    Example 2 - Provide details of all the orders with a quantity greater than 10.
    The SQL command will be something like this:
    SELECT * FROM SALES_TABLE WHERE QUANTITYORDERED > 10;
    Ensure that the SQL code does not have triple backticks at the beginning or end, and the output should not contain the word "sql."
    """
]

## Streamlit App
st.set_page_config(page_title="I am SQL-Gemini",page_icon="🔮")
st.header("Gemini App To Retrieve SQL Data")
question=st.text_input("Input: ",key="input")
submit=st.button("Submit Query")
st.subheader("Example Queries:")
st.write("1. Retrieve details of orders with a quantity greater than 15, limited to 5 rows")
st.write("2. Get the total sales for each product line")
st.write("4. Get the average sales for each product line")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"sales_database.db")
    st.success("Query executed successfully. Results displayed here.")
    for row in response:
        st.header(row)
