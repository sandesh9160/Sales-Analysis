import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection string
connection_string = 'mysql+pymysql://root:root@localhost:3333/exceldb'

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Write your SQL query
query = "SELECT * FROM excelapp_exceldata"

# Fetch data into a DataFrame
df = pd.read_sql_query(query, engine)

# Export DataFrame to Excel
df.to_excel("exceldata.xlsx", index=False)
