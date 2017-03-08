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
        #TODO : Add random selection of pivot ?
        pivot = my_list[0]
        left, right = [], []
        for x in my_list[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':

    if 0:
        l = np.random.randint(1, 10, 10)
        print("List to sort : {}".format(l))
        sorted_l = quick_sort(l)
        print( "List sorted : {}".format(sorted_l))

    if 1:
        l = [1, 4, 5, 5, 5, 8, 8, 10, 0, -1, -2, 10, 9]
        print("List to sort : {}".format(l))
        sorted_l = quick_sort(l)
        print("List sorted : {}".format(sorted_l))
