#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps = 0
    for idx in range(len(a)):
        curr = 0
        while curr < len(a) - 1:
            if a[curr] > a[curr + 1]:
                a[curr], a[curr + 1] = a[curr + 1], a[curr]
                swaps += 1
            curr += 1
    print("Array is sorted in",swaps,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
