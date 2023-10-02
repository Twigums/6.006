"""
Problem 4, part b.

Given an array A of strictly increasing integers of length n, and a number s, your task is to design
an algorithm to find the smallest integer larger than or equal to s not in A.
"""

"""
The idea is to binary search to either:
    1. find where s fits in A
    2. find s in A
If s exists in A:
    1. binary search towards where the first gap where elements are incremented by > 1;
        i. if both sides of search are shown to have consistent +1 increments, return last element of array + 1
        ii. if search ends with [..., a, b, ...] with pointers i, j for a, b; return A[i] + 1
"""

"""
find_first_missing_element()
inputs: an array, A; an integer, s
output: smallest integer, x >= s not in A

the function binary searches for either:
    1. where s will fit
        - if this is the case, then function will return x = s
    2. where s is
        - if this is the case, then function will return a call to the function "incrementSearch()"
"""
def find_first_missing_element(A, s):

    n = len(A) # define n as the number of elements in array, A

    # for this binary search, two pointers, left and right, are chosen and defined as such
    left = 0
    right = n - 1

    # loop that continues until the difference of right - left >= 0
    # for each loop, the middle index is calculated and s will be compared to A[middle]
    # then, the corresponding pointers will be inclusively moved accordingly
    # for the case s == A[middle], it will return a call to "incrementSearch()"
    while right - left >= 0:

        middle = left + (right - left) // 2

        if s > A[middle]:
            left = middle + 1

        elif s < A[middle]:
            right = middle - 1

        else:
            return incrementSearch(A, middle)

    # if the while loop is exited, that means s has not been found by the binary search, so we can safely return x = s
    return s

"""
incrementSearch()
inputs: an array, A; an integer, point (the previous pointer to where "s" is in A)
output: smallest integer, x > s not in A

this is a helper function for the second binary search
the idea for this search is to find the first gap after the index of s in A where the elements have a difference of > 1
this means that the smallest value can be returned
there are two return conditions for this function:
    1. if A[point:n] is an increasing array where each element is incremented by 1 (ex: [1, 2, 3, 4]), then the function will return the last element + 1 (A[n - 1] + 1)
    2. if the search concludes with the pointers pointing to two elements that has a gap in between, then the function will return the left element + 1 (A[left] + 1)
"""
def incrementSearch(A, point):

    n = len(A) # define n as the number of elements in array, A

    # similar to above function;
    # this time left is our minimum bounds
    left = point
    right = n - 1

    # similar to above function
    # but this time, we compare middle to both left and right indices as well as A[middle] to A[left] and A[right] respectively
    # if they are not the same, then that means a gap must exist in that side of the array
    # otherwise, it will return the maximum value in the array + 1
    while right - left >= 0:

        middle = left + (right - left) // 2

        if left + 1 == right:
            return A[left] + 1

        if middle - left != A[middle] - A[left]:
            right = middle

        elif right - middle != A[right] - A[middle]:
            left = middle

        else:
            return A[n - 1] + 1

    return None # to cover bases
