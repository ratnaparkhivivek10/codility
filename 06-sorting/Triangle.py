# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    # write your code in Python 3.6
    for p, q, r in combinations(range(len(A)), 3):
        if A[p] + A[q] > A[r] and A[q] + A[r] > A[p] and A[r] + A[p] > A[q]:
            return 1
    else:
        return 0
