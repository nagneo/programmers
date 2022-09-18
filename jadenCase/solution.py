# 프로그래머스 
# 코딩테스트 > 연습문제 > JadenCase 문자열 만들기 
# Level 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    words = [(word.capitalize() if word and word[0].isalpha() else word.lower()) for word in s.split(" ")]
    return " ".join(words)

#print(solution("3people unfollowed   me"))