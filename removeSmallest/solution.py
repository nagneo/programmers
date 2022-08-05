def solution(arr):
  
    min = min(arr);
    arr.remove(min)
    return [arr] if len(arr) > 0 else [-1]