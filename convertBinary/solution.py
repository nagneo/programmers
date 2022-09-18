# 프로그래머스 
# 코딩테스트 > 월간 코드 챌린지 시즌1 > 이진변환 반복하기 
# Level 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
  convertCnt = 0
  zeroCnt = 0
  while(int(s) > 1):
    cnt, removed = removeZero(s);
    zeroCnt += cnt
    s = "{0:b}".format(int(len(removed)))
    convertCnt += 1
  
  return [convertCnt, zeroCnt]

def removeZero(s):
  cnt = 0;
  result = ""
  for ch in s:
    if ch == "0":
      cnt += 1
    else:
      result += ch
  
  return cnt, result

print(solution("110010101001"))