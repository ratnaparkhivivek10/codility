# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    return len(list(filter(lambda x: x%K == 0, range(A, B+1))))
