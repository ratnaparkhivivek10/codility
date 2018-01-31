# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations

def solution(A):
    # write your code in Python 3.6
    slice_data = {}
    for item in combinations(range(len(A)), 2):
        d = A[item[0]:item[1]+1]
        slice_data[item] = sum(d)/len(d)
    
    return min(slice_data.keys(), key=lambda t: slice_data.get(t))[0]
