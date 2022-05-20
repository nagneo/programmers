def solution(s):
    
    slen = len(s)
    m = slen // 2
    return s[m-1:m+1] if slen % 2 == 0 else s[m]

print(solution("abcde"))
print(solution("qwer"))