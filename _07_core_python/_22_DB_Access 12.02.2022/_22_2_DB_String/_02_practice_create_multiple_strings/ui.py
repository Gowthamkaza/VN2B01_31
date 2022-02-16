'''
Req : get username and username length and exempt numeric and special characters
save to Data Base

'''


from controller import get_str_len

if __name__ == '__main__':

    str1 = input("username: ")
    resp = get_str_len(str1)
    print("input user length:", resp)