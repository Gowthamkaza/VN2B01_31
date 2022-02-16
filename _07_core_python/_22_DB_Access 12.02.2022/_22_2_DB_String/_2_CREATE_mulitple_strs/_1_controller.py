from ._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        st_len = get_len(in_str)
        return st_len


