import copy as cp
import numpy as np

"""
    Insertion sort

    Time complexity :
    ----------------
    - average O(n^2)
    - worst case O(n^2) : when list sorted in reverse order
    - best case O(n) : when list already sorted

    Space complexity : O(1)
    -----------------

"""

def insertion_sort(my_list, order='ascending', in_place=True):
    """
       Takes a list/np.array of integers and sort the given list in the
       ascending/descending order given the value of ascending

       :param my_list: list, np.array | List to sort
       :param order: basestring | Set to 'ascending' or 'descending'
       :param in_place: boolean | If list sorted in place
       :return: list, np.array | Sorted list
    """

    # check arguments passed
    if not isinstance(my_list, (list, np.ndarray)):
       raise TypeError("Argument to selection_sort must be a list or array.")
    if not order in ['ascending', 'descending']:
        raise IOError('"order" argument must be either "ascending" or  \
                                                                "descending"')

    if not in_place:
        my_list = cp.copy(my_list)

    def _insert(seq, k):
        if k >= 1:
            if seq[k-1] > seq[k]:
                seq[k-1], seq[k] = seq[k], seq[k-1]
                return _insert(seq, k-1)

    for i in range(1, len(my_list)):
        _insert(my_list, i)

    # Sort in ascending or descending order
    order_dict = {'ascending': 1, 'descending': 0}
    my_list = my_list[::2*order_dict[order]-1]

    if not in_place:
        return my_list

def insertion_sort2(my_list):
    """
    Implementation of the insertion sort as seen
    in professor Eleni Drinea's Algorithm for Data Science class
    :param my_list: list | list to sort
    :return: sorted list
    """
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j+1] = key
    return my_list


if __name__ == '__main__':

    if 0:
        l = np.random.randint(1, 10, 10)
        print("List to sort : {}".format(l))
        sorted_l = insertion_sort(l, in_place=False)
        print( "List sorted : {}".format(sorted_l))

    if 0:
        l = [1, 4, 5, 5, 5, 8, 8, 10, 0, -1, -2, 10, 9]
        print("List to sort : {}".format(l))
        sorted_l = insertion_sort(l, in_place=False)
        print("List sorted : {}".format(sorted_l))

    if 1:
        l = [1, 4, 5, 5, 5, 8, 8, 10, 0, -1, -2, 10, 9]
        print("List to sort : {}".format(l))
        sorted_l = insertion_sort2(l)
        print("List sorted : {}".format(sorted_l))
