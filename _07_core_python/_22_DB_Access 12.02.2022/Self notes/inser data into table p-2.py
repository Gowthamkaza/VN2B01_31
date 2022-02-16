import psycopg2

conn=psycopg2.connect(host="localhost",
                      port="5432",
                      user="postgres",
                      password="1234")
coursor=conn.cursor()
records1="insert into gowtham4 values(1,ram,9630245689)"
records2="insert into gowtham4 values(2,rajesh,9656856789)"
records3="insert into gowtham4 values(3,rithvik,9857856789)"
coursor.execute(records1)
coursor.execute(records2)
coursor.execute(records3)
conn.commit()
print("record inserted succesfully")
