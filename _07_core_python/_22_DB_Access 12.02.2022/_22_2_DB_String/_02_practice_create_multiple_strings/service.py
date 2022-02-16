from dao import save_to_db

def get_len(str_val):
    le = 0
    for each in str_val:
        le += 1
    save_to_db(str_val, each)
    return le