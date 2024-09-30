import pyodbc
from app.azure.secerts import get_customer_sql_secret
def get_db_connection():
    connection_string = (
    get_customer_sql_secret
    )
    return pyodbc.connect(get_customer_sql_secret())
