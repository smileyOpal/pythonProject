#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput

# An avid hiker keeps meticulous records of their hikes.
# During the last hike that took exactly 'steps' steps,
# for every step it was noted if it was an uphill, 'U', or
# a downhill, 'D' step. Hikes always start and end at sea level,
# and each step up or down represents a 1 unit change in altitude.
# We define the following terms:
#
# > A mountain is a sequence of consecutive steps above sea level, starting
# with a step up from sea level and ending with a step down to sea level.
# > A valley is a sequence of consecutive steps below sea level, starting
# with a step down from sea level and ending with a step up to sea level.
#
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
#
# Example
# steps = 8
# path = DDUUUUDD
#
# The hiker first enters a valley 2 units deep.Then they climb out and up onto
# a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.
# Result is hiker traversed 1 valley


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley_count = 0
    start_count = False
    sea_level = 0
    for step in list(path):
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1

        if not start_count and sea_level < 0:
            start_count = True
        elif start_count and sea_level >= 0:
            start_count = False
            valley_count += 1

    return valley_count


# Write your code here

if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(" ")
        print "solution #1 result is {0}".format(countingValleys(input[0], input[1]))



# 1 > 8 UDDDUDUU
# 2 > 12 DDUUDDUDUUUD
