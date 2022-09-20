def solution(n):
    return fibonacciLoop(n) % 1234567

# recursive
# 정확성 42.9 / 100
def fibonacci(n):
    if n == 1: 
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-2) + fibonacci(n-1)
      
# for
# 정확성 100.0 / 100
def fibonacciLoop(n):
  ppre = 0
  pre = 1
  answer = 0
  for i in range(2, n+1):
    answer = ppre + pre
    #for next set
    ppre = pre
    pre = answer
  
  return answer

# test 
print(solution(5))
print(solution(3))