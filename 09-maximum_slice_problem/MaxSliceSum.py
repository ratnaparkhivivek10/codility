# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations_with_replacement as cwr
def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    else:
        return max((sum(A[p:q+1]) for p, q in cwr(range(len(A)), 2)))
