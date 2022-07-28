def solution(s):
    pCnt = 0;
    yCnt = 0;
    for ch in s:
        ch = ch.lower()
        if ch == 'p':
            pCnt += 1
        if ch == 'y':
            yCnt += 1
        
    return pCnt == yCnt