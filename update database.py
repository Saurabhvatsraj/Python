import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='Saurabh@23',
              database='college')

cursor= con.cursor()
name=input("enter the name")
age=int(input("enter the  age"))

query="update student set name='{}' where age={}".format(name,age)

cursor.execute (query)
con.commit()
print("update data successfully")
