# 프로그래머스
# 코딩테스트 연습 > 스택/큐 > 올바른 괄호
# Level 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
  bracket = []
  
  for ch in s:
    if ch == "(":
      bracket.append(ch)
    elif ch == ")":
      if not bracket:
        return False
      popped = bracket.pop()
      if popped != "(":
        return False
  
  return len(bracket) == 0
  
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))