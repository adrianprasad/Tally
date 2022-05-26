import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='testdb'
    )
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE Tally(Date DATE,Particulars VARCHAR(255),VchType VARCHAR(255),vchNo VARCHAR(255), DebitAmount INT, CreditAmount Int)')
