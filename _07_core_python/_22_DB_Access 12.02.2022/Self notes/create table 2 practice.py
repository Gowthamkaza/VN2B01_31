import psycopg2

conn=psycopg2.connect(host="localhost",
                      port="5432",
                      user="postgres",
                      password="1234")
cursor=conn.cursor()
cursor.execute("drop table if exists gowtham4")
quary="create table gowtham4(S_no varchar(10),name varchar(30),mobile_no bigint)"
cursor.execute(quary)
rec1 = "insert into gowtham4 values('1', 'gowtham', 6346238567)"
rec2 = "insert into gowtham4 values('2', 'ram', 6345688567)"
rec3 = "insert into gowtham4 values('3', 'ravi', 6344763567)"
cursor.execute(rec1)
cursor.execute(rec2)
cursor.execute(rec3)
conn.commit()
print("the table is created")