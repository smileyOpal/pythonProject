#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would
# become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation.
# This is called a circular array.
#
# Given an array 'a' of 'n' integers and a number, 'd', perform 'd' left rotations on the array.
# Return the updated array to be printed as a single line of space-separated integers.
#
# Function Description
# Complete the function rotLeft in the editor below.
# rotLeft has the following parameter(s):
# > int a[n]: the array to rotate
# > int d: the number of rotations
#
# Returns
# int a'[n]: the rotated array

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    if d > len(a):
        if d % len(a) == 0:
            return a
        else:
            d = d % len(a)

    result = a[d:]
    result = result + a[0:d]
    return result

# Write your code here

if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(" ")
        array_data = [int(numeric_string) for numeric_string in input[1:]]
        print "result is {0}".format(rotLeft(array_data, int(input[0])))


# 1999 1 2 3 4 5 6 7        > result is [5, 6, 7, 1, 2, 3, 4]
# 4 1 2 3 4 5               > result is [5, 1, 2, 3, 4]