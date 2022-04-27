import operator

def solution(N, stages):
    
    answer = []
    failRateMap = {}
    for n in range(1,N+1):
        rate = 0
        total = [i for i in stages if i >= n];
        if len(total) == 0:
            rate = 0
        else:
            failure = [j for j in total if j == n]
            rate = len(failure) / len(total);
        
        failRateMap[n] = rate
        
    sorted_dict = sorted(failRateMap.items(), key=operator.itemgetter(1),reverse=True)
    for p in sorted_dict:
        answer.append(p[0])
        
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))