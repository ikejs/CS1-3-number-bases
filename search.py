#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index == len(array):
        return None
    if item == array[index]:
        return index
    index += 1
    return linear_search_recursive(array, item, index)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        if item < array[mid]:
            right = mid - 1
        if item > array[mid]:
            left = mid + 1
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    if left > right:
        return None
    mid = (left + right) // 2
    if array[mid] == item:
        return mid
    if item < array[mid]:
        # right = mid - 1
        return binary_search_recursive(array, item, left, mid-1)
    if item > array[mid]:
        # left = mid + 1
        return binary_search_recursive(array, item, mid+1, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests