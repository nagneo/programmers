from itertools import combinations

def solution(numbers):
    return sorted(set([sum(item) for item in combinations(numbers, 2)]))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))