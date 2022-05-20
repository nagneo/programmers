def solution(d, budget):
    sum = 0
    answer = 0
    d.sort()
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1
        else: break;
    
    return answer

#print(solution([1,3,2,5,4], 9))
#print(solution([2,2,3,3], 10))
