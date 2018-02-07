# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if A:
        dominator = max(A, key=A.count)
        if A.count(dominator) > len(A)/2:
            return A.index(dominator)
        else:
            return -1
    else:
        return -1
