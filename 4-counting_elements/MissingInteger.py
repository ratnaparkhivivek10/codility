# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if all([i < 0 for i in A]):
        return 1
    else:
        mn, mx = min(A), max(A)
        if mn < 0:
            for i in range(1, mx+2):
                if i not in A:
                    return i
        else:
            for i in range(1, mx+2):
                if i not in A:
                    return i
                    
# Performance of this solution is not ok(codility score: 25%), need to optimize the soultion in future.                    
