""" File name:   math_functions.py
    Author:      Longfei Zhao
    Date:        23.2.2017
    Description: This file defines a set of variables and simple functions.

                 It should be implemented for Exercise 1 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import math

ln_e = math.e
twenty_radians = math.radians(20)

def quotient_ceil(numerator, denominator):
    '''
        return the ceiling of the numerator divided by the denominator
    '''
    return math.ceil(numerator / denominator)

def quotient_floor(numerator, denominator):
    '''
        return the floor of the numerator divided by the denominator
    '''
    return math.floor(numerator / denominator)

def manhattan(x1, y1, x2, y2):
    '''
        returns the Manhattan distance between the two points
    '''
    return math.hypot(x1 - x2, y1 - y2)
