
import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()

    records = [(101, 'MADHU', 'ABC'), (102, 'Prakash', 'AREM'), (103, 'Kiran', 'VN2')]
    query = "INSERT INTO STUDENT VALUES(%s, %s, %s)"
    for record in records:
        cursor.execute(query, record)
    '''
    #Step3 : Prepare sql query
    rec1 = "INSERT INTO STUDENT_321 VALUES(101, 'MADHU', 'ABC')"
    rec2 = "insert into student_321 values(102, 'Prakash', 'AREM')"
    rec3 = "insert into STUDENT_321 values(103, 'Kiran', 'VN2')"
    # Step4 : Execute sql query
    cursor.execute(rec1)
    cursor.execute(rec2)
    res = cursor.execute(rec3)
    print("Insertion : ", res)
    '''
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()



'''
%S -
Passing parameters to a SQL statement happens in functions such as Cursor.execute() 
by using %s placeholders in the SQL statement, and passing a sequence of values as 
the second argument of the function

'''