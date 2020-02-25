import re


def check_name_valid(name):
    if re.search(r'\d', name):
        return False
    return True
