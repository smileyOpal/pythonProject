#!/bin/python3

from math import trunc
from collections import Counter
import os
import random
import re
import sys
import fileinput


# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
#
# Example
# n =7
# ar = [1,2,1,2,1,3,2]
#
# There is one pair of color  and one of color. There are three odd socks left,
# one of each color. The number of pairs is .
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = {}
    for a in ar:
        if pairs.get(a, None) is None:
            pairs[a] = 1
        else:
            pairs[a] = pairs[a] + 1
    return sum(trunc(pairs[item] / 2) for item in pairs)


def sockMerchant2(n, ar):
    int_list = map(int, ar)
    counter = Counter(int_list)
    return sum(trunc(counter[c] / 2) for c in counter)


if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(",")
        array_size = input[0]
        array_data = [int(numeric_string) for numeric_string in input[1:]]
        print "solution #1 result is {0}".format(sockMerchant(array_size, array_data))
        print "solution #2 result is {0}".format(sockMerchant2(array_size, array_data))
