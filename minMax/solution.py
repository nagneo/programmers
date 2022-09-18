# 프로그래머스 
# 코딩테스트 > 연습문제 > 최댓값과 최솟값
# Level 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    list = [int(i) for i in s.split()]
    answer = f'{min(list)} {max(list)}'
    return answer
