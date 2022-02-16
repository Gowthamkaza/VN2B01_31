from dao import save_to_db

def get_length(str1):
    print("_____service layer_____")
    data = str1.split()
    c_data = data[0: -1]
    user_id = data[-1]
    print("service layer :", c_data, user_id)
    words = {}
    for word in c_data:
        le = 0
        for char in word:
            le += 1
        word = word.upper()
        words[word] = le
        print("service layers :: words length", words)
        f_words = list(words.keys())
        f_words.sort()
        word_len = len(words.keys())
        print("service layer final data:", user_id, f_words, word_len)
        res = save_to_db(user_id, f_words, word_len)
        if res :
            return user_id, words
        else:
            return "error happened"






