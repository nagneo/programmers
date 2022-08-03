def solution(s):
    answer = ''
    index = 0
    for ch in s:
        if ch == ' ':
            answer += ' '
            index = -1
        else:
            if index & 1: #odd
                answer +=  ch.lower()
            else:
                answer += ch.upper()
        index += 1
          
    return answer