import psycopg2

conn = psycopg2.connect(host="localhost",
                        port="5432",
                        user="postgres",
                        password="1234")
cursor = conn.cursor()
quary = "create table if not exists gowtham(age varchar(3),mobile_no varchar(10))"
cursor.execute(quary)
conn.commit()


