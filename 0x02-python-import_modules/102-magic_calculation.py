#!/usr/bin/python3
def magic_calculation(a, b):
    # import add and sub from magic_calculation_102 module
    from magic_calculation_102 import add, sub
    # if a is less than b, do the following
    if a < b:
        # initialize c as the sum of a and b
        c = add(a, b)
        # loop from 4 to 6 (excluding 6)
        for i in range(4, 6):
            # add i to c and update c
            c = add(c, i)
        # return c
        return c
    # otherwise, do the following
    else:
        # return the difference of a and b
        return sub(a, b)
