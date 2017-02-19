import copy as cp
import numpy as np

"""
    Selection sort

    Time complexity :
    ----------------
    - average O(n^2)
    - worst case O(n^2)
    - best case O(n^2)

    Space complexity : O(1)
    ----------------

"""

def selection_sort(my_list, order='ascending',
                                    in_place=True, verbose=False):
    """
       Takes a list/np.array of integers and sort the given list in the
       ascending/descending order given the value of ascending

       :param my_list: list, np.array | List to sort
       :param order: basestring | Set to 'ascending' or 'descending'
       :param in_place: boolean | If list sorted in place
       :param verbose: boolean | True to print the different steps of the
                                    sorting process
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

    for i in range(len(my_list) - 1):
        ind_min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[ind_min]:
                ind_min = j
        if not ind_min:  # if my_list[i] is the minimum
            continue

        if verbose:
            # print the pivot and the minimum in square brackets
            print("Step %i" % (i + 1))
            print([[v] if k == i or k == ind_min else v
                                            for k, v in enumerate(my_list)])

        # switch values in positions i and ind_min
        my_list[i], my_list[ind_min] = my_list[ind_min], my_list[i]

    # Sort in ascending or descending order
    order_dict = {'ascending': 1, 'descending': 0}
    my_list = my_list[::2*order_dict[order]-1]

    if not in_place:
        return my_list


if __name__ == '__main__':

    if 0:
        l = np.random.randint(1, 10, 10)
        print("List to sort : {}".format(l))
        sorted_l = selection_sort(l, in_place=False, verbose=True)
        print( "List sorted : {}".format(sorted_l))

    if 1:
        l = [1, 4, 5, 5, 5, 8, 8, 10, 0, -1, -2, 10, 9]
        print("List to sort : {}".format(l))
        sorted_l = selection_sort(l, in_place=False, verbose=True)
        print("List sorted : {}".format(sorted_l))
