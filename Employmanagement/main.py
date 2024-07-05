import mysql.connector

con = mysql.connector.connect(
    host = "localhost", user = "root", password = "password", database = "emp"
)

def check_employee(employee_id):
    #Query to select all rows from the employess table where id matches
    sql = 'SELECT * FROM employees WHERE id=%s'
    #Making cursor buffered to make rowcount method work properly
    cursor = con.cursor(buffered=True)
    data = (employee_id,)
    
    #Executing the sql query
    cursor.execute(sql,data)
    #Fetch the first row to cehck if employee exists
    employee = cursor.fetchone()
    #closing the cursor
    cursor.close()
    
    return employee is not None

def add_emmployee():
    Id = input("Enter Employee ID : ")
    
    if check_employee(Id):
        print("Employee already exists. please try agian")
        return
    else:
        Name = input("Enter Employee Name: ")
        Post = input("ENter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
        
        sql = 'INSERT INTO employess(id, name, position, salary) VALUES (%s, %s %s, %s)'
        data = (Id, Name, Post,Salary)
        cursor = con.cursor()
        
        try:
            #executing the sql query
            cursor.execute(sql, data)
            
            #committing the transaction
            con.commit()
            print("Employee Added Successfully")
        except mysql.connector.Error as err:
            print(f"Error:{err}")
            con.rollback()
        finally:
            cursor.close()

def remove_employee():
    Id = input("Enter Employee ID: ")
    
    #Checking if employee with given Id exists
    if not check_employee(Id):
        print("Employee dooes not exist")
        return
    else:
        #Query to delete employee from the employees table
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()
        
        try:
            cursor.execute(sql, data)
            
            con.commit()
            print("Employee Removed Successfully")
            
        except mysql.connector.Error as err:
            print(f"Error {err}")
            con.rollback()
        finally:
            cursor.close()
def promote_employee():
    Id = input("Enter Employee's Id : ")
    
    if not check_employee(Id):
        print("Employee does not exist")
        return
    else:
        try:
            Amount = float(input("Enter increase in Salary: "))
            
            #query to Fettch salary of employee with given id
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (id,)
            cursor = con.cursor()
            
            cursor.execute(sql_select,data)
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount
            
            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            data_update =(new_salary,Id)
            
            cursor.execute(sql_update,data_update)
            
            con.commit()
            print("Employee Promoted")
        except (ValueError,mysql.connector.Error) as e:
            print(f"Error : {e}")
            con.rollback()
        finally:
            cursor.close()

def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor = con.cursor()
        
        cursor.execute()
        
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name: ", employee[1])
            print("Empployee Post: ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------")
    except mysql.connector.Error as err:
        print(f"Error : {err}")
    
    finally:
        cursor.close()
        
def menu():
    while True:
        print("\n Welcome to Employee Management Record")
        print("Press: ")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote EMployee")
        print("4 to Display Employee")
        print("5 to Exit")
        
        ch = input("Enter Your Choice: ")
        
        if ch =="1":
            add_emmployee()
        elif ch == "2":
            remove_employee()
        elif ch == "3":
            promote_employee()
        elif ch == "4":
            display_employees()
        elif ch == "5":
            print("Exiting the program")
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    menu()