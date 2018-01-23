# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    return 1 if sorted(A) == list(range(1, len(A)+1)) else 0
