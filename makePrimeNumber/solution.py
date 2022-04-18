#https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    answer = 0
    list = [i for i in combinations(nums, 3)]
    for set in list:
        s = sum(set)
        isPrime = True;
        for n in range(2,s):
            if s % n == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1

    return answer


#print(solution([1,2,3,4]))
#print(solution([1,2,7,6,4]))