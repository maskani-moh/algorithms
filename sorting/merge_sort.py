import copy as cp
import numpy as np

"""
    Merge sort

    Time complexity :
    ----------------
    - average O(n*log(n))
    - worst case O(n*log(n))

    Space complexity :
    -----------------
    - best case O(1)

"""

def merge_sort(my_list, in_place=True, order='ascending'):
    """
       Takes a list/np.array of integers and sort the given list

       :param my_list: list, np.array | List to sort
       :return: list, np.array | Sorted list
    """

    # check arguments passed
    if not isinstance(my_list, (list, np.ndarray)):
       raise TypeError("Argument to selection_sort must be a list or array.")

    if not in_place:
        my_list = cp.copy(my_list)

    n = len(my_list)

    if n <= 1:
        if not in_place:
            return my_list

        # Sort in ascending or descending order
        order_dict = {'ascending': 1, 'descending': 0}
        my_list = my_list[::2 * order_dict[order] - 1]

        return my_list
    else:
        return merge(merge_sort(my_list[: int(np.floor(n/2.))]),
                     merge_sort(my_list[int(np.floor(n/2.)):]))


def merge(seq_1, seq_2):
    """
    Merge two lists so that the resulting list is an ordered list

    :param seq_1: list, np.array | left list
    :param seq_2:  list, np.array | right list
    :return: list | merged list
    """
    if len(seq_1) == 0:
        return seq_2
    if len(seq_2) == 0:
        return seq_1

    res = []
    k, l = 0, 0
    while k < len(seq_1) and l < len(seq_2):
        if seq_1[k] <= seq_2[l]:
            res.append(seq_1[k])
            k += 1
        else:
            res.append(seq_2[l])
            l += 1

    # concatenate what remains
    res += seq_1[k:]
    res += seq_2[l:]
    return res


if __name__ == '__main__':

    if 0:
        l = np.random.randint(1, 10, 10)
        print("List to sort : {}".format(l))
        sorted_l = merge_sort(l, in_place=False)
        print( "List sorted : {}".format(sorted_l))

    if 1:
        l = [1, 4, 5, 5, 5, 8, 8, 10, 0, -1, -2, 10, 9]
        print("List to sort : {}".format(l))
        sorted_l = merge_sort(l, in_place=False)
        print("List sorted : {}".format(sorted_l))
