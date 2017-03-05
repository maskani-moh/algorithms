import copy as cp
import numpy as np

"""
    Quick sort

    Time complexity :
    ----------------
    - average O(n*log(n))
    - worst case O(n^2)

    Space complexity :
    -----------------
    - best case O(1)

"""

# TODO : add inplace method + descending order
def quick_sort(my_list):
    """
    Takes a list of integers and sort it.

    :param my_list: list | List of integers to sort
    :return: list | sorted list
    """
    if len(my_list) <= 1:
        return my_list
    else:
        pivot = my_list[0]
        left, right = [], []
        for x in my_list[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)
