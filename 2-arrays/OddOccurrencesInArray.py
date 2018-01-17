# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from functools import reduce
def solution(A):
    # write your code in Python 3.6
    return reduce(lambda x, y: x^y, A)
