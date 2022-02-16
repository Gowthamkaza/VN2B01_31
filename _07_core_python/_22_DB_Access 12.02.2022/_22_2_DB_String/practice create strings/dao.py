from utils import conn


def save_to_db(u_id, words, length):
    try:
        cursor = conn.cursor()
        query = "insert into user_307 values(%s, %s, %s)"
        print("inserted data in db:", u_id, words, length)
        cursor.execute(query, (u_id, words, length))
        conn.commit()
        return True
    except Exception as exce:
        print("Exception occurred as :", exce)
    finally:
        print("cursor and connections are closed and data sent to DB")
        cursor.close()
        conn.close()
