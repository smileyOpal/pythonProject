#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


def minimumBribes(q):
    count = 0
    base = [i for i in range(1, len(q) + 1)]
    match = False
    is_chaos = False
    while not match and not is_chaos:
        for p in q:
            base_index = base.index(p)
            target_index = q.index(p)
            diff = base_index - target_index
            if diff == 0:
                continue
            elif diff > 2:
                is_chaos = True
            # print('----- p {0} diff {1}'.format(p, diff))
            for j in range(diff):
                base_index = base.index(p)
                swapPositions(base, base_index - 1, base_index)
                count += 1
            #     print('{0}-{1} > {2}'.format(base_index, base_index - 1, base))
            # print('----- new {0}'.format(base))
        match = base == q

    if is_chaos:
        print('Too chaotic')
    else:
        print('{0}'.format(count))


def minimumBribes2(q):
    count = 0
    is_chaos = False

    q_pos = max(q)
    while q_pos > 0 and not is_chaos:
        current = q.index(q_pos)
        diff = current - q_pos + 1
        # print('----- p {0} index {1} diff {2}'.format(q_pos, current, diff))
        if diff < -2:
            is_chaos = True
            break
        elif diff != 0:
            for i in range(abs(diff)):
                swapPositions(q, current, current + 1)
                current += 1
                count += 1
            # print('----- new {0}'.format(q))

        q_pos -= 1

    if is_chaos:
        print('Too chaotic')
    else:
        print('{0}'.format(count))


def minimumBribes3(q):
    count = 0
    is_chaos = False

    for i, val in enumerate(q):
        if val - i - 1 > 2:
            is_chaos = True
            break

        for j in range(max(val - 2, 0), i):
            print('i q[{0}]={1} ---- j q[{2}]=[{3}]'.format(i, q[i], j, q[j]))
            if q[j] > val:
                count += 1

        print('---- count {0}'.format(count))

    if is_chaos:
        print('Too chaotic')
    else:
        print('{0}'.format(count))


if __name__ == '__main__':
    for line in fileinput.input():
        input = line.rstrip().split(" ")
        array_data = [int(numeric_string) for numeric_string in input[0:]]
        minimumBribes3(array_data)

# 3     2 1 5 3 4
# X     2 5 1 3 4
# X     5 1 2 3 7 8 6 4
# 7     1 2 5 3 7 8 6 4
# 4     1 2 5 3 4 7 8 6

