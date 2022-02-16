import psycopg2

conn=psycopg2.connect(Database="postgres",
                      host="localhost",
                      port="5432",
                      user="postgres",
                      password="1234")
cursor=conn.cursor()
query="select * from gowtham4"
cursor.execute(query)