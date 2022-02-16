from utils import conn     # DAO - Data Access Object


def save_to_db(i_str, le):

    try:
        cursor = conn.cursor()
        query = "INSERT INTO vn_307 values(%s, %s)"
        cursor.execute(query, (i_str, le))
        conn.commit()
    except Exception as exce:
        print("Exception occurred as", exce)
    finally:
        cursor.close()
        conn.close()

