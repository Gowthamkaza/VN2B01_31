from .utils import  conn


def save_to_db(i_str, le):
    try:

        cursor = conn.cursor()
        query = "INSERT INTO user_307 VALUES(%s,%s)"
        cursor.execute(query, (i_str, le))
        conn.commit()
    except Exception as e:
        print("Exception details : ", e)
    finally:
        cursor.close()
        conn.close()
