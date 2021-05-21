#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# There is a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus.
# The player can jump on any cumulus cloud having a number that is equal to
# the number of the current cloud plus 1 or 2. The player must avoid the thunderheads.
# Determine the minimum number of jumps it will take to jump from the starting
# postion to the last cloud. It is always possible to win the game.
#
# For each game, you will get an array of clouds numbered 0
# if they are safe or 1 if they must be avoided.
#
# Example
# c = [0,1,0,0,0,1,0]
# Index the array from 0...6. The number on each cloud is its index in the list
# so the player must avoid the clouds at indices 1 and 5. They could follow these
# two paths: 0>2>4>6 or 0>2>3>4>5. The first path takes 3 jumps while the second takes 4.
# Return 3.


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

# c = [0,1,0,0,0,1,0]
def jumpingOnClouds(c):
    jump = 0
    converted = [str(c_int) for c_int in c]
    join_clouds = "".join(converted)
    end = False

    while not end:
        index = join_clouds.find('1')
        clouds = len(join_clouds[0:index])
        if index < 0:
            end = True
            clouds = len(join_clouds[0:])

        jump = jump + math.trunc(clouds / 2) + 1
        join_clouds = join_clouds[index + 1:]

    return jump - 1


if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(" ")
        array_data = [numeric_string for numeric_string in input[0:]]
        result = jumpingOnClouds(array_data)
        print "result is {0}".format(result)

# 28 > 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0
#  3 > 0 0 0 1 0 0
#  4 > 0 0 1 0 0 1 0
