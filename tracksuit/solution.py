def solution(n, lost, reserve):
    uniqueLost = set(lost) - set(reserve)
    uniqueReserve = set(reserve) - set(lost)
    for i  in uniqueReserve:
        if i - 1 in uniqueLost:
            uniqueLost.remove(i-1)
        elif i + 1 in uniqueLost:
            uniqueLost.remove(i+1)
    answer = n - len(uniqueLost)
    
    return answer

#print(solution(5, [2,4], [1,3,5]))
#print(solution(5, [2,4], [3]))
#print(solution(3, [3], [1]))
