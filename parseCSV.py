import pandas as pd
import numpy as np
from mods.config import *
from mysqlconnection import connectToMySQL     # import the function that will return an instance of a connection

def parseCSV(filePath):
    # Database
    mydb = connectToMySQL()
    # CVS Column Names
    col_names = ['RUT', 'NOMBRE', 'CUSTOM1', 'CUSTOM2', 'CUSTOM3', 'CUSTOM4', 'CUSTOM5']
    # Use Pandas to parse the CSV file
    data = pd.read_excel(filePath,usecols=col_names, sheet_name=0)
    df_data = data.replace(np.nan, '', regex=True)
    # Loop through the Rows
    for i,row in df_data.iterrows():
        query = "INSERT INTO nomina_usuarios (rut, nombre, custom1, custom2, custom3, custom4, custom5) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (str(row['RUT']),str(row['NOMBRE']),str(row['CUSTOM1']),str(row['CUSTOM2']),str(row['CUSTOM3']),str(row['CUSTOM4']),str(row['CUSTOM5']),)
        mydb.query_db(query,params)
        print(i,str(row['RUT']),str(row['NOMBRE']),str(row['CUSTOM1']),str(row['CUSTOM2']),str(row['CUSTOM3']),str(row['CUSTOM4']),str(row['CUSTOM5']))