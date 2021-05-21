#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput
from collections import Counter


# There is a string, 's', of lowercase English letters that is repeated
# infinitely many times. Given an integer, 'n', find and print the number
# of letter a's in the first 'n' letters of the infinite string.
#
# Example
# s = 'abcac'
# n = 10
#
# The substring we consider is abcacabcac, the first 10 characters of the infinite string.
# There are 4 occurrences of a in the substring.

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a_count = s.count('a')
    count_full_loop_a = math.trunc(n/len(s)) * a_count
    left_over_string = n % len(s)
    extra_a = s[0:left_over_string].count('a')
    return count_full_loop_a + extra_a


if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(" ")
        print "result is {0}".format(repeatedString(input[0], int(input[1])))


# 7                 > aba 10
# 1000000000000     > a 1000000000000
# 1                 > avia 3
# 0                 > sdvc 10
