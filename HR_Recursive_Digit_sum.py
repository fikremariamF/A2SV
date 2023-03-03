#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    # n *= k
    # print("mmy n" ,n)
    if len(n) > 1:
        new_n = 0
        for num in n:
            new_n += int(num)
        return superDigit(str(new_n * k), 1)
    else:
        # print("final", n)
        return n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
