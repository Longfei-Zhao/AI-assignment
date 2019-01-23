""" File name:   truth_tables.py
    Author:      Longfei Zhao
    Date:        23.2.2017
    Description: This file defines a number of functions which implement Boolean
                 expressions.

                 It also defines a function to generate and print truth tables
                 using these functions.

                 It should be implemented for Exercise 2 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""

def boolean_fn1(a, b, c):
    ''' returns the truth value of (a ∨ b) → (-a ∧ -b)
    '''
    return not (a or b)

def boolean_fn2(a, b, c):
    ''' returns the truth value of (a ∧ b) ∨ (-a ∧ -b)
    '''
    return (a and b) or ( not a and not b)

def boolean_fn3(a, b, c):
    ''' returns the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b)
    '''
    return (a and not b) or (not a and b)

def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None
    """
    print("a     b     c     res\n-----------------------")
    Bools = [0, 1]
    Bools_print = ["False", "True "]
    for a in Bools:
        for b in Bools:
            for c in Bools:
                res = boolean_fn(a, b, c)
                print(Bools_print[a], Bools_print[b], Bools_print[c], Bools_print[res])
