def solution(s, n):
    answer = ''
    for ch in s:   
        if ch == ' ':
            answer += ' ';
        else:
          ciphered = chr(ord(ch) + n)
          num = ord(ciphered) 
          if ch.isupper() and num > ord('Z'):
            ciphered = chr(num - 26)
          elif ch.islower() and num > ord('z'):
            ciphered = chr(num - 26)
          answer += ciphered
    
    return answer


#solution('z', 1)