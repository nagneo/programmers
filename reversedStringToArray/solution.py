def solution(n):
    answer = []
    reversed = str(n)[::-1]
    
    return [int(i) for i in reversed]
  
#print(solution(12345))