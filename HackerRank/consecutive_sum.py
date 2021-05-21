#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# Given a long integer, find the number of ways to represent if as
# a sum of two or more consecutive positive integers
# Example: num =21
#
# There are 3 ways to represent num = 21 as the sum of two or more consecutive integers:
# 1+2+3+4+5+6 = 21
# 6+7+8 = 21
# 10+11 = 21

def consecutive(N):
    count = 0
    L = 1
    while L * (L + 1) < 2 * N:
        a = (1.0 * N - (L * (L + 1)) / 2) / (L + 1)
        if a - int(a) == 0.0:
            count += 1
        L += 1
    return count


def consecutive_2(N):
    start = 1
    end = (N + 1) / 2 + 1
    count = 0

    while start < end:
        sum = 0
        for i in range(start, end):
            sum += i
            if sum == N:
                count += 1
            elif sum > N:
                break
        start += 1
    return count


if __name__ == '__main__':
    for line in fileinput.input():
        requirement = int(line.rstrip())
        print "result is {0}".format(consecutive(requirement))
        print "result is {0}".format(consecutive_2(requirement))
