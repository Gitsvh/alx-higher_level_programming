#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    return [replace if num == search else num for num in my_list]
