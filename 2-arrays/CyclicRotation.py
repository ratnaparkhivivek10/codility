# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    dq = deque(A)
    dq.rotate(K)
    
    return list(dq)
