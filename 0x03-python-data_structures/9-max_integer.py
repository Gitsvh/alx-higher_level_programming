#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if my_list == []:
        return(None)
    my_list.sort()
    return(my_list[-1])
