#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        ascii_val = ord(c)
        if 97 <= ascii_val <= 122:
            uppercase_c = chr(ascii_val - 32)
        else:
            uppercase_c = c
        uppercase_str += uppercase_c
    print("{}".format(uppercase_str))
