# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    # write your code in Python 3.6
    if A:
        profit = (A[q] - A[p] for p, q in combinations(range(len(A)), 2))
        return max(0, *profit)
    else:
        return 0
