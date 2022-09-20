def solution(n):
    startN = 1
    tryCount = 1
    answer = 0
    while startN >= 1:
        startN = tryGetStartInt(n, tryCount)
        #정수이면
        if startN >= 1 and int(startN) == startN:
            answer += 1   
        tryCount += 1
    
    return answer

# 정수로 나누어떨어지는지 확인
def tryGetStartInt(n, count):
    return (n - sum(range(count))) / count
  
print(solution(15))