def solution(nums):
    picked = set()
    max = len(nums) // 2
    for n in nums:
        if n not in picked:
            picked.add(n)
            if max == len(picked):
                break;
            
    answer = len(picked)
    return answer

#print(solution([3,1,2,3]))
#print(solution([3,3,3,2,2,4]))
#print(solution([3,3,3,2,2,2]))