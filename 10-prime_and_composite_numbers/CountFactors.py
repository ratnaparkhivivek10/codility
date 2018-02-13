# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# O(n) complexity
def solution(N):
    # write your code in Python 3.6
    return len([n for n in range(1, N+1) if N%n == 0])
