import pymysql.cursors
from datetime import date

con=pymysql.connect(
    host="localhost",
    user="root",
    password="priya",
    database="attendance")
cursor=con.cursor()

#add employee
def add_emp():
    emp_id=int(input("Enter employee id:"))
    name=input("Enter employee name:")
    cursor.execute("SELECT * FROM emp WHERE emp_id=%s", (emp_id,))
    if cursor.fetchone():
        print("Employee ID already exists!")
        return
    emp="INSERT INTO emp(emp_id,name)values(%s,%s)"
    values=(emp_id,name)
    cursor.execute(emp,values)
    con.commit()
    print('Employee add scuccessfully')

#search employee
def search_emp():
    emp_id=int(input("Enter employee id:"))
    emp="select * from emp where emp_id=%s"
    values=(emp_id,)
    cursor.execute(emp,values)
    result=cursor.fetchone()
    if result:
        print("Employee found")
    else:
        print("Employee Not Found")
    print()

#update employee
def update_emp():
    emp_id=int(input("Enter employee id:"))
    cursor.execute("SELECT * FROM emp WHERE emp_id=%s", (emp_id,))
    if cursor.fetchone() is None:
        print("Employee ID does not exist!")
        return
    name=input("Enter employee name:")
    emp="update emp set name=%s where emp_id=%s"
    values=(name,emp_id)
    cursor.execute(emp,values)
    con.commit()
    print("Employee update Successfully")

#delete employee
def delete_emp():
     emp_id=int(input("Enter employee id to delete:"))
     cursor.execute("SELECT * FROM emp WHERE emp_id=%s", (emp_id,))
     if cursor.fetchone() is None:
        print("Employee ID does not exist!")
        return
     emp="delete from emp where emp_id=%s"
     values=(emp_id,)
     cursor.execute(emp,values)
     con.commit()
     print("Employee Deleted")

#mark attendance
def mark_attendance():
    emp_id=int(input("Enter employeee id:"))
    status=input("Enter status(Present/Absent):")
    today=date.today()
    cursor.execute("SELECT * FROM emp WHERE emp_id=%s", (emp_id,))
    if cursor.fetchone() is None:
        print("Employee ID does not exist!")
        return
    
    check = "SELECT * FROM attendance WHERE emp_id=%s AND date=%s"
    cursor.execute(check, (emp_id, today))
    record = cursor.fetchone()
    if record:
        print("Attendance already marked for today!")
    else:
        emp = "INSERT INTO attendance(emp_id, date, status) VALUES (%s, %s, %s)"
        cursor.execute(emp, (emp_id, today, status))
        con.commit()
        print("Attendance Marked")
   
#Mark Leave
def mark_leave():
    emp_id=int(input("Enter employee id:"))
    leave_type=input("Enter leave type(CL/SL/PL):")
    today=date.today()
    cursor.execute("SELECT * FROM emp WHERE emp_id=%s", (emp_id,))
    if cursor.fetchone() is None:
        print("Employee ID does not exist!")
        return
    check = "SELECT * FROM attendance WHERE emp_id=%s AND date=%s"
    cursor.execute(check, (emp_id, today))
    record = cursor.fetchone()

    if record:
        print("Attendance/Leave already marked for today!")
    else:
        emp = "INSERT INTO attendance(emp_id, date, status) VALUES (%s, %s, %s)"
        cursor.execute(emp, (emp_id, today, leave_type))
        con.commit()
        print("Leave Recorded")
 
    

#View All Attendance
def all_attendance():
    cursor.execute("select * from attendance")
    rows=cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Emp ID: {row[1]} | Date: {row[2]} | Status: {row[3]}")
    else:
        print("No attendance records found.")
    print()

#view attendance by employee
def view_attendance():
    emp_id=int(input("Enter employee id:"))
    emp="select* from attendance where emp_id=%s"
    values=(emp_id,)
    cursor.execute(emp,values)
    rows=cursor.fetchall()
    if rows:
        print("\nAttendance Records:")
        print("ID | Emp ID | Date       | Status")
        print("-----------------------------------")
        
        for row in rows:
            print(f"{row[0]}  |  {row[1]}     | {row[2]} | {row[3]}")
    else:
        print("No attendance records found for this employee.")
    
    print()
    
# view today attendance
def view_tdyattendance():
    today = date.today()
    query = "SELECT * FROM attendance WHERE date = %s"
    cursor.execute(query, (today,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Emp ID: {row[1]} | Date: {row[2]} | Status: {row[3]}")
    else:
        print("No attendance records for today.")

    print()


#delete attendance record
def delete_attendance():
    record_id=int(input("Enter attendance record id:"))
    emp="delete from attendance where id=%s"
    cursor.execute("SELECT * FROM attendance WHERE id=%s", (record_id,))
    if cursor.fetchone() is None:
        print("Record ID does not exist!")
        return
    values=(record_id,)
    cursor.execute(emp,values)
    con.commit()
    print("Record Deleted")

#Monthly Attendance report

def monthly_report():
    emp_id=int(input("Enter employee id:"))
    month=int(input("Enter Month(MM):"))
    year=int(input("Enter year(yyyy):"))
    query="""SELECT status, COUNT(*)
        FROM attendance
        WHERE emp_id=%s AND MONTH(date)=%s AND YEAR(date)=%s
        GROUP BY status"""
    cursor.execute(query, (emp_id, month, year))
    rows = cursor.fetchall()
    print("Monthly Report")
    for row in rows:
        print(f"{row[0]}:{row[1]}days")
    print()

while True:
    print("Employee Attendance System")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee Name")
    print("4. Delete Employee")
    print("5. Mark Attendance")
    print("6. Mark Leave (CL/SL/PL)")
    print("7. View All Attendance")
    print("8. View Attendance by Employee")
    print("9. View Today’s Attendance")
    print("10. Delete Attendance Record")
    print("11. Monthly Attendance Report")
    print("12. Exit")

    choice=int(input("Enter Your Choice"))
    if choice==1:
        add_emp()
    elif choice==2:
        search_emp()
    elif choice==3:
        update_emp()
    elif choice==4:
        delete_emp()
    elif choice==5:
        mark_attendance()
    elif choice==6:
        mark_leave()    
    elif choice==7:
        all_attendance()
    elif choice==8:
        view_attendance()
    elif choice==9:
        view_tdyattendance()
    elif choice==10:
        delete_attendance()
    elif choice==11:
        monthly_report()
    elif choice==12:
        print("Exiting Program")
        break
    else:
        print("Invalid Choice!Try Again")

    


               

    

    
    

     
     
    
    
    
