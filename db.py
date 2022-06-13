
import mysql.connector
class Database:
    # making Connection
    def __init__(self):
        self.con = mysql.connector.connect(
        host="localhost", user="root", password="12345678", database="Tally")

    
    def Display(self,Table):
    
        # query to select all rows from
     
        sql = 'select * from ' + Table
        c = self.con.cursor()

        # Executing the SQL Query
        c.execute(sql)

        r = c.fetchall()
        return r
            
db=Database()
# result=db.Display('table')
# print (result)