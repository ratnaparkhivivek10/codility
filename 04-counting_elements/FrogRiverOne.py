# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    posn = set()
    for index, item in enumerate(A):
        posn.add(item)
        if len(posn) == X:
            return index
    else:
        return -1
            
