
import mysql.connector
class Database:
    # making Connection
    def __init__(self):
        self.con = mysql.connector.connect(
        host="localhost", user="root", password="12345678", database="employee")

    
    def Display_Employees(self,table):
    
        # query to select all rows from
        # Employee Table
        sql = 'select * from ' + table 
        c = self.con.cursor()

        # Executing the SQL Query
        c.execute(sql)

        # Fetching all details of all the
        # Employees
        r = c.fetchall()
        return r

    def check_employee(self,employee_id):
    
        # Query to select all Rows f
        # rom employee Table
        sql = 'select * from empd where id=%s'

        # making cursor buffered to make
        # rowcount method work properly
        c = self.con.cursor(buffered=True)
        data = (employee_id,)

        # Executing the SQL Query
        c.execute(sql, data)

        # rowcount method to find
        # number of rows with given values
        r = c.rowcount
        if r == 1:
            return True
        else:
            return False
    
    def Add_Employ(self, employee_data):
    
        if(self.check_employee(employee_data[0]) == True):
            print("Employee aready exists\nTry Again\n")

        else:

            # Inserting Employee details in
            # the Employee Table
            sql = 'insert into empd values(%s,%s,%s,%s)'
            c = self.con.cursor()
            # Executing the SQL Query
            c.execute(sql, employee_data)
            # commit() method to make changes in
            # the table
            self.con.commit()
            print("Employee Added Successfully ")
    
    def Remove_Employee(self,Id):
            # Checking if Employee with given Id Exist
        # or Not
        if(self.check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
        else:
            # Query to Delete Employee from Table
            sql = 'delete from empd where id=%s'
            data = (Id,)
            c = self.con.cursor()

            # Executing the SQL Query
            c.execute(sql, data)

            # commit() method to make changes in
            # the table
            self.con.commit()
            print("Employee Removed")
            
db=Database()
result=db.Display_Employees('empd')
print (result)