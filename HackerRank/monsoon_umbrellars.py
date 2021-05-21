#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# Given a number of people N and an array of integers, each one representing the amount
# of people a type of umbrella can handle, output the minimum number of umbrellas
# needed to handle N people.

# No umbrella could have left spaces. Which means if a umbrella can handle 2 people,
# there should be 2 people under it.
# If there's no solution, return -1.


def getUmbrellas(requirement, sizes):
    umbrellas = filter(lambda x: 0 < x <= requirement, sizes)
    umbrellas.sort(reverse=True)
    if requirement == 0:
        return -1

    result = 0
    for u in umbrellas:
        umbrella_count = requirement / u
        if umbrella_count > 0:
            result += umbrella_count

        requirement = requirement - (u * umbrella_count)

        if requirement == 0:
            break

    if requirement > 0:
        return -1

    return result


if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(",")
        requirement = int(input[0])
        array_size = input[1]
        array_data = [int(numeric_string) for numeric_string in input[2:]]
        result = getUmbrellas(requirement, array_data)
        print "result is {0}".format(result)

# | no. of people   | size  | umbrellas sizes array | answer    |
# | 1               | 2     | 3,5                   | -1        |
# | 3               | 2     | 3,5                   | 1         |
# | 3               | 2     | 1,2                   | 2         |
# | 10              | 2     | 3,1                   | 4         |
