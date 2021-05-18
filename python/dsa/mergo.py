class Merge:

    def __init__(self, _list):
        self._list = _list

    def __ascender__(self):
        return self._list


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2

    print(f'merge_sort(arr, left_index={left_index}, middle={middle}), right_idx={right_index}')
    merge_sort(array, left_index, middle)

    print(f'merge_sort(arr, middle+1={middle+1}, right_idx={right_index})')
    merge_sort(array, middle + 1, right_index)

    print(f'merge(arr, left_idx={left_index}, right_idx={right_index}, middle={middle})')
    merge(array, left_index, right_index, middle)
    print(array)
    print('')


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    print('Merge Fun, left-copy=', left_copy, 'right-copy=',right_copy, '', end='')

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


if __name__ == '__main__':
    from time import time
    from copy import deepcopy
    all_lists = [
        [12, 5, 99, 1, 36],
        [12, 44, 66, 99, 33, 11, 55],
        [69, 11, 88, 14, 16, 369, 199, 99, 116, 188]
    ]
    dcopy = deepcopy(all_lists)
