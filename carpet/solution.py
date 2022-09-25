def solution(brown, yellow):
  #이차 방정식을 이용하여 근의 공식으로 풀기
  b = 0.5 * (brown + 4)
  c = brown + yellow
  width = 0.5 * (b + (b * b - 4 * 1 *c) ** (1/2)) 
  height = c / width 
  
  return [width, height]