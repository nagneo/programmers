import math 

def solution(n):
    array = [True for i in range(n + 1)]
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    return sum(i for i in array if array[i] == True) - 2
            