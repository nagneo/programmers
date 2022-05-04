def solution(n):
    answer = 0
    reversed = getReversedTernaryNumeralSystem(n)
    length = len(reversed) 
    for i, ch in enumerate(reversed):
        answer += int(ch) * (3 ** (length - i - 1))
        
    return answer

def getReversedTernaryNumeralSystem(n):
    result = ""
    while n > 0:
        t = n % 3
        n = int(n / 3)
        result+=str(t)
        
    return result
    
#print(solution(45))