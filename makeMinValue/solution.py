# 프로그래머스 
# 코딩테스트 연습 > 연습문제 > 최솟값 만들기
# Level 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    
    A = sorted(A, reverse = True)
    B = sorted(B)
    multiplied = [a * b for a, b in zip(A, B)]
    return sum(multiplied)

print(solution([1, 4, 2], [5, 4, 4]))