def solution(n):
    arr = sorted(list(str(n)), reverse=True)
    return int(''.join(arr))
  
#print(solution(118372))