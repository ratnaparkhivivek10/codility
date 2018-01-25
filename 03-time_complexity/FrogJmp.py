#This is brute force solution, can be optimized by using other approaches.
def solution(X, Y, D):
    # write your code in Python 3.6
    jumps, dist_covered = 0, X
    while dist_covered < Y:
        dist_covered += D
        jumps += 1
        
    return jumps
