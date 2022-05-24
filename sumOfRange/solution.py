def solution(a, b):
    count = abs(a-b) + 1
    return count * (a + b) / 2

# def solution(a, b):
#     if a == b:
#         answer = a
#     elif a < b:
#         answer = sum(range(a,b+1))
#     else:
#         answer = sum(range(b,a+1))
    
#     return answer