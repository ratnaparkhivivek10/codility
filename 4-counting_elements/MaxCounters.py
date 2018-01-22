# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    data = [0]*N
    for i in A:
        try:
            data[i-1] += 1
        except IndexError:
            data = [max(data)]*N
    
    return data
