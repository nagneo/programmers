def solution(price, money, count):

    sum = 0
    for i in range(1, count + 1):
        sum += i * price
    
    return abs(money - sum) if sum > money else 0

#print(solution(3,20,4))