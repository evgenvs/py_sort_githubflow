#!/usr/bin/env python
#
#  Python example of using sorting algorithm and GitHub flow for working with source code. Source is here:
#
#  https://github.com/evgenvs/py_sort_githubflow
#



def bubbleSort(alist):
    for nums in range(len(alist)-1,0,-1):
        for i in range(nums):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist


def insertionSort(alist):
    for j in range(1, len(alist)):
        key = alist[j]
        i = j-1
        while i>=0 and alist[i] > key:
            alist[i+1] = alist[i]
            i-=1
        alist[i+1] = key
    return alist
