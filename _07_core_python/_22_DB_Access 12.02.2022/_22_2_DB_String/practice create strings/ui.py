'''
REQ:  Find length of each word  in a string(, separated) and store the results to db
Criteria: User will give string along with his userid.
          Last word in the string can be considered as userid
hello,world,welcome,to,python,MadhuNettem

output: hello - 5
        world - 6
        ....
CRUD            - Create, Retrieve
Data types      - string int
STATE, BEHAVIOR -

'''

from controller import get_str_length


if __name__ == '__main__':

    str1 = 'hello, welcome, to, vnsquare, vn307'
    print("calling controller layer")
    resp = get_str_length(str1)
    print("ui layer - Final response", resp)
    print("--UI Layer :: Welcome Mr : ", resp['user_id'])
    print("--UI Layer :: Total words : ", resp['st_len'])
    print("--UI Layer :: Word details  : ")
    for word in resp['words']:
        print(word, "----", len(word))


