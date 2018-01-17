def solution(N):
    data = bin(N)[2:].strip('0').split('1')
    bg = max(data, key=lambda d: len(d))
    if bg:
        return len(bg)
    else:
        return 0