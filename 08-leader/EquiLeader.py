# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    leader = max(A, key=lambda x: A.count(x))
    equi_leaders = 0
    for i in range(1, len(A)):
        seq1, seq2 = A[:i], A[i:]
        
        if seq1.count(leader) > len(seq1)/2 and seq2.count(leader) > len(seq2)/2:
            equi_leaders += 1
    
    return equi_leaders
