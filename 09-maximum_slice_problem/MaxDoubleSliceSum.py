# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    # write your code in Python 3.6
    slice_length = []
    for x, y, z in combinations(range(len(A)), 3):
        slice_length.append(sum(A[x+1: y]) + sum(A[y+1:z]))
        
    return max(slice_length)
