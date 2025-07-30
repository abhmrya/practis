import mysql.connector
class UserLogin:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='student'
        )
        # print('Successfully connected:', self.db)
    def show_tables(self):
        self.cur = self.db.cursor()  # Store cursor separately (do not overwrite self.db)
        self.cur.execute("SHOW TABLES")
        for table in self.cur:
            print(table)

    def create_acc(self, userid, password):
        self.cur = self.db.cursor()
        query = "INSERT INTO student (userid, password) VALUES (%s, %s)"
        try:
            self.cur.execute(query, (userid, password))
            self.db.commit()  # Ensure commit is called on the database connection
            print("Account created successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)

    def show_table(self):
        self.cur = self.db.cursor()
        query = "SELECT * FROM student"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    
    def edit_student(self, userid, password,ids):
        query="update student set userid=%s,password=%s where userid=%s"
        self.cur=self.db.cursor()
        self.cur.execute(query,(userid,password,ids))
        self.db.commit()
        self.cur.close() 
        print("succesfully edit student  id.")


    def log_in(self):
        query="SELECT * FROM student WHERE password=%s"
        cur = self.db.cursor()
        cur.execute(query,('Abhay@321',))
        rows=cur.fetchone()
        if rows:
            for row in rows:
                print(row)
        else:
            print("no password is match.")


    def delete_student(self,userid):
        query='delete from student  where  userid=%s'
        self.cur=self.db.cursor()
        self.cur.execute(query,(userid,))
        self.db.commit()
        print('successfullay delete teh student id')

def create_acc():
    login = UserLogin()
    userid=input("enter the userid")
    password=input("enter the password")
    login.create_acc(userid,password)

def studentlogin():
    login = UserLogin()
    border()
    print("01.show the tables.")
    print("1.create account")
    print('2.show the table')
    print("3.sign in")
    print('4.edit the student id & password.')
    print("5.delete the student login ")
    choice=input("what is your choice?")
    if choice =='01':
        border()
        login.show_tables()
    elif choice=='1':
        border()
        create_acc()
    elif choice=='2':
        border()
        login.show_table()
    elif choice=='3':
        border()
        login.log_in()
    elif choice=='4':
        border()
        user=input('Enter new user id.')
        password=input('Enter the new password')
        ids=input('Enter your present id')
        login.edit_student(user,password,ids)
    elif choice=='5':
        border()
        userid=input('Enter the student id')
        login.delete_student(userid)

class Details:
    def __init__(self):
        self.dbm = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='details'
        )
    def student_details(self,name,claxx,age,cource,address):
        query="insert into details(name,claxx,age,cource,address) values(%s,%s,%s,%s,%s)"
        try:
            self.cur=self.dbm.cursor()
            self.cur.execute(query,(name,claxx,age,cource,address))
            self.dbm.commit()
            print("successfuly fill the Details.")
        except:
            print("error something else.")
 
    def details_of_student(self,name,age):
        query="select * from details where name=%s and age=%s"
        self.cur=self.dbm.cursor()
        self.cur.execute(query,(name,age))
        details = self.cur.fetchall()
        for row in details:
            print(row)

    def delete_details(self,username):
        query='delete from details where name=%s'
        self.cur=self.dbm.cursor()
        self.cur.execute(query,(username,))
        self.dbm.commit()
        print('successfullay delete teh details.')

    def edit_details(self,username,claxx,age,cource,address,ids):
        query="update details set name=%s,claxx=%s,age=%s,cource=%s,address=%s where name=%s"
        self.cur=self.dbm.cursor()
        self.cur.execute(query,(username,claxx,age,cource,address,ids))
        self.dbm.commit()
        self.cur.close() 
        print("succesfully edit details  id.")


def fill_details():
    details=Details()
    username=input("Enter the student name.")
    claxx=input("enter the student class name.")
    age=input("Enter the student age.")
    cource=input("Enter the student cource name.")
    address=input("Enter the student addresh name.")
    details.student_details(username,claxx,age,cource,address)


def chek_details():
    details=Details()
    name=input("Enter the user name.")
    age=input("Entr the age.")
    details.details_of_student(name,age)


def details():
    details=Details()
    print('1.fill the student details')
    print('2.chek the details')
    print('3.delete the details.')
    print('4.edit the details.')
    choice=input("enter thr your choice")
    if choice=='1':
        border()
        fill_details()
    elif choice=='2':
        border()
        chek_details()
    elif choice=='3':
        border()
        username=input('Enter the username')
        details.delete_details(username)
    elif choice=='4':
        border()
        username=input('Enter the new username.')
        claxx=input('Enter the new class name.')
        age=input('Enter the new age.')
        cource=input('Enter the new cource name')
        address=input('Enter the new address.')
        ids=input("Enter the present id.")
        details.edit_details(username,claxx,age,cource,address,ids)


class Marks:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Marks'
        )
    
    def student_marks(self,userid,math,science,hindi,english,drawing):
        query="insert into  marks(id,math,science,hindi,english,drawing) values(%s,%s,%s,%s,%s,%s)"
        try:
            self.cur=self.db.cursor()
            self.cur.execute(query,(userid,math,science,hindi,english,drawing))
            self.db.commit()
            print("marks added successfully!")
        except:
            print("No data fill in marks")

    def seen_marks(self,userid):
        query="select * from marks where id=%s"
        try:
            self.cur=self.db.cursor()
            self.cur.execute(query,(userid,))
            marks=self.cur.fetchall()
            for mark in marks:
                print(mark)
        except:
            print('something error:')
    
    def edit_marks(self,userid,math,science,hindi,english,drawing):
        query="update marks set math=%s,science=%s,hindi=%s,english=%s,drawing=%s where id=%s"
        self.cur=self.db.cursor()
        self.cur.execute(query,(math,science,hindi,english,drawing,userid))
        self.db.commit()
        self.cur.close() 
        print("succesfully edit marks.")
        seen_mark()
    def delete_marks(self,userid):
        query='delete from marks where id=%s'
        self.cur=self.db.cursor()
        self.cur.execute(query,(userid,))
        self.db.commit()
        print('successfullay delete teh details.')

def marks_student():
    marks=Marks()
    print("Fill the student marks data  ")
    userid=input('Enter the student id  ')
    math=input('Enter the student marks of math  ')
    science=input('Enter the student marks of science ')
    hindi=input('Enter the student marks of hindi ')
    english=input('Enter the student marks of english ')
    drawing=input('Enter the student marks of drawing ')
    marks.student_marks(userid,math,science,hindi,english,drawing)

def seen_mark():
    marks=Marks()
    userid=input("enter the your marks id.")
    marks.seen_marks(userid)
    

def edit_marks():
    marks=Marks()
    border()
    userid=input('Enter the student id  ')
    math=input('Enter the student marks of math  ')
    science=input('Enter the student marks of science ')
    hindi=input('Enter the student marks of hindi ')
    english=input('Enter the student marks of english ')
    drawing=input('Enter the student marks of drawing ')
    marks.edit_marks(userid,math,science,hindi,english,drawing)
    


def marks():
    marks=Marks()
    border()
    print('1.Enter the marks ')
    print('2.show the marks: ')
    print('3.Edit the marks')
    print('4.Delete Marks')
    choice=input('Enter thr your choice.')
    if choice=='1':
        marks_student()
    elif choice=='2':
        seen_mark()
    elif choice=='3':
        edit_marks()
    elif choice=='4':
        userid=input("Enter the user id.")
        marks.delete_marks(userid)

def border():
    print(50*'*')

def main():
    print("1.student login")
    print('2.student details.')
    print('3.student Marks')
    choice=input('Enter the your choice: ')
    if choice=='1':
        border()
        studentlogin()
    elif choice=='2':
        border()
        details()
    elif choice=='3':
        border()
        marks()
main()
