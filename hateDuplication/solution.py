def solution(arr):
    result = []
    pre = -1
    for i in arr:
        if pre == i:
            continue
        else:
            result.append(i)
            pre = i
            
    return result

print(solution([1,1,3,3,0,1,1,2]))
print(solution([4,4,4,3,3]))