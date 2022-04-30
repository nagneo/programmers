def solution(p):
    answer = ''
    
    if not p:
        return ''; 
    
    # 문자열 분리
    left = 0
    right = 0
    u = ''
    v = ''
    for i, ch in enumerate(p):
        if ch == '(':
            left += 1
        else: right += 1
        
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break;
    
    # U 가 올바른 괄호 문자열인가
    if isCorrectBracket(u):
        fixed = solution(v)
        return u + fixed;
    # U 가 올바른 괄호 문자열이 아닌 경우
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = u[1:-1]
        u = u.replace('(', 't').replace(')','(').replace('t', ')') #swap
        result += u
        return result
        

def isCorrectBracket(p):
    left = 0
    right = 0
    for ch in p:
        if ch == '(':
            left += 1
        else: 
            right += 1
            
        if left >= right:
            continue
        else: return False
    
    return True


# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))