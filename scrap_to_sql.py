import pyodbc
import pandas as pd

server = '(local)'
db = 'ReportServer'

conn = pyodbc.connect(driver='{SQL Server}',host=server,database=db,
                      trusted_connection='yes',user='User')

sql = "SELECT * FROM Table_webscrap"

df = pd.read_sql(sql, conn)
print(df.head())