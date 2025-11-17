#!/usr/bin/python3
def zipping_data(list1, list2):
    zipped_data = zip(list1, list2)
    zipped_list = list(zipped_data)

    for item in zipped_list:
        print("{}: R$ {:.2f}".format(item[0], item[1]))
