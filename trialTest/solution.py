from pickle import TRUE


def solution(answers):
    answer = []
    order1 = [1,2,3,4,5]
    order2 = [2,1,2,3,2,4,2,5]
    order3 = [3,3,1,1,2,2,4,4,5,5]
    surrenderMap = {1:0, 2:0, 3:0}
    
    for i, ans in enumerate(answers):
        if ans == order1[i % len(order1)]:
            surrenderMap[1] += 1
        if ans == order2[i % len(order2)]:
            surrenderMap[2] += 1
        if ans == order3[i % len(order3)]:
            surrenderMap[3] += 1
     
    surrenderMap = sorted(surrenderMap.items(), key=lambda x: x[1], reverse = True)
    max = 0
    for item in surrenderMap:
        if item[1] > max:
            max = item[1]
        
        if max == item[1]:
            answer.append(item[0])
        
    return answer.sort()


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))