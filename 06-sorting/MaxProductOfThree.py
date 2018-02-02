# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    # write your code in Python 3.6
    return max((A[p]*A[q]*A[r] for p, q, r in combinations(range(len(A)), 3)))
