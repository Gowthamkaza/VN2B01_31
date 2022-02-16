import psycopg2

conn = psycopg2.connect(host="localhost",
                        port="5432",
                        user="postgres",
                        password="1234")
print("Connection object : ", type(conn), conn)
cur = conn.cursor()

cur.execute("Insert into Gowtham2(SNO,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Gowtham', 27, 'india'50000.00 )");

cur.execute("Insert into Gowtham2(SNO,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Basi reddy', 20, 'india', 50000.00 )");

cur.execute("Insert into Gowtham2 (SNO,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Uday', 30, 'india', 20000.00 )");


conn.commit()
print ("Records created successfully");
conn.close()