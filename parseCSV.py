import pandas as pd
from mods.config import *
from mysqlconnection import MySQLConnection     # import the function that will return an instance of a connection

def parseCSV(filePath, mydb):
    # CVS Column Names
    col_names = ['RUT', 'NOMBRE', 'CUSTOM1', 'CUSTOM2', 'CUSTOM3', 'CUSTOM3', 'CUSTOM5']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    # Loop through the Rows
    for i,row in csvData.iterrows():
        sql = "INSERT INTO addresses (first_name, last_name, address, street, state, zip) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (row['first_name'],row['last_name'],row['address'],row['street'],row['state'],str(row['zip']))
        with mydb.cursor() as cursor:
            cursor.execute(sql, value, if_exists='append')
            mydb.commit()
        print(i,row['RUT'],row['NOMBRE'],row['CUSTOM1'],row['CUSTOM2'],row['CUSTOM3'],row['CUSTOM4'],row['CUSTOM5'],)