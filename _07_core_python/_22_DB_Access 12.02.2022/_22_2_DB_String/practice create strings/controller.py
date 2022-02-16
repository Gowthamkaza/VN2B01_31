from service import get_length

def get_str_length(str1):
    print("controller layer")
    if str1 == ' ':
        return "Enter valid string"
    else:
        word_data = get_length(str1)
        print("controller response", word_data)
        return {'user_id': word_data[0],
                'st_len': len(word_data[1].keys()),
                'words': list(word_data[1].keys())
                }
