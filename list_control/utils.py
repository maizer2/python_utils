import os
from typing import List

def difference_set_to_list(list1: List, list2: List) -> List:
    set1 = set(list1)
    set2 = set(list2)
    diff = set1 - set2
    return list(diff)
 
def difference_set_to_set(list1: List, list2: List) -> set:
    set1 = set(list1)
    set2 = set(list2)
    diff = set1 - set2
    return diff

def list_str_remove(list1: List, prefix: str) -> List:
    for i in range(len(my_list)):
        my_list[i] = my_list[i].replace(prefix, '', 1)
    return my_list
