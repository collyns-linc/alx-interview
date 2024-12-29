#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Pascal triangle solution that takes a n argument
and returns the nth row of the Pascal triangle.
"""


def pascal_triangle(n):
    """
    Pascal triangle solution that takes a n argument
    and returns the nth row of the Pascal triangle.
    """
    my_list = []
    if n > 0:
        my_list.append([1])
        for i in range(1, n):
            x = my_list[i - 1]
            my_list.append([1] + [x[j] + x[j + 1]
                                  for j in range(len(x) - 1)] + [1])

        return my_list
    else:
        return my_list
