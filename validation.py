import re


def is_valid_uid(uid):
    return (
        re.match(r'^[a-zA-Z\d]{10}$', uid) and
        re.search(r'(?:[^A-Z]*[A-Z][^A-Z]*){2,}', uid) and
        re.search(r'(?:[^\d]*\d[^\d]*){3,}', uid) and
        not re.search(r'(.).*?\1', uid)
    )
for _ in range(0, int(raw_input())):
    if is_valid_uid(raw_input().strip()):
        print 'Valid'
    else:
        print 'Invalid'
    
