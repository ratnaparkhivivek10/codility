# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    impact_factor = {'A':1, 'C':2, 'G':3, 'T':4}
    
    return [impact_factor[k] for k in list(map(lambda p, q: min(S[p:q+1], key=lambda x: impact_factor.get(x)), P, Q))]
