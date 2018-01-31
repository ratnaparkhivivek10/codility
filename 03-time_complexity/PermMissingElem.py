# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    return 1 if not A else sum(range(1, len(A)+2)) - sum(A)
