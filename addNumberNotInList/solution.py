#https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    list = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        list.remove(num)
    
    answer = sum(list)
    return answer

#print(solution([1,2,3,4,6,7,8,0])) #14