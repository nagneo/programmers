#import math

def solution(n, m):
    
    #return [math.gcd(n,m), math.lcm(n,m)]
    # 유클리드 호제법
    gcd = getGCD(n, m)
    return [gcd, int(n * m / gcd)]

def getGCD(n,m):
  if m == 0:
    return n
  else:
    return getGCD(m, n % m)
  
#print(solution(3,12))
#print(solution(2,5))