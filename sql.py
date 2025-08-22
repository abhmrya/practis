import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Admin",
      database="test"
    )
print(mydb,'\n')
mycursor = mydb.cursor()

querys=['select * from student',
    'select * from student where class>23',
    "select * from student where name like 'a%'",
        "select * from student where name like '%a'",
    "select * from student where name like 'a%y'",
    "select * from student where name like '_b%'",
    "select * from student where name like '__h%'",
    "select * from student where name like 'a_%'",
    "select * from student where name like '%a_'",
    "select * from student where id between 2 and 5",
    "select * from student where id not between 2 and 5",
    "select * from student where id between 2 and 5 order by id desc",
    "select * from student where id between 2 and 5 ",
    "select * from student as a cross join teacher as t ",
    "select * from student where age in (20) or name in ('abhay')"
    ]
for q in querys:
    try:
        mycursor.execute(q)

        # Fetch data + column names
        rows = mycursor.fetchall()
        columns = [desc[0] for desc in mycursor.description]
        # Print table
        print(q)
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        print('\n')
    finally:
        pass
