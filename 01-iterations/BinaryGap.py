def solution(N):
    data = bin(N)[2:].strip('0').split('1')
    bg = max(data, key=lambda d: len(d))
    if bg:
        return len(bg)
    else:
        return 0
    
# Second approach.
def solution(N):
    data = bin(N)[2:]
    print(data)
    count = 0
    max = 0
    for i in data:
        if i == '0':
            count+=1
        else:
            if max < count:
                max = count
                count = 0
            else:
                count = 0
    return max
