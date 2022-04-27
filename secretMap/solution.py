#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i, current in enumerate(arr1):
        b = arr2[i]
        res = bin(current | b)
        answer.append((res).replace('0b','').zfill(n).replace('1', '#').replace('0', ' '))
    return answer


#print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
#print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))