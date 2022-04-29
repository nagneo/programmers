def solution(s):
    answer = 0
    min = len(s);
    length = int(len(s) / 2 + 1)
    for n in range(1, length):
        list = [ s[i:i+n] for i in range(0, len(s), n)]
        compressed = ""
        keyMap = {}
        for i, str in enumerate(list):
            if len(str) < n:
                #종료 - todo
                compressed += popCompressed(keyMap)
                compressed += str
                break;
            if i + 1 == len(list):
                #종료 - todo
                addedStr = popCompressed(keyMap)
                if addedStr:
                    compressed += addedStr
                else:
                    compressed += str
                break;
            
            keyMap.setdefault(str, 1)
            if str == list[i + 1]:
                keyMap[str] += 1
            else:
                compressed += popCompressed(keyMap)
            #print(i, str)
        
        if min > len(compressed):
            min = len(compressed)    
      
    answer = min  
    return answer

def popCompressed(keyMap):
    if keyMap:
        item = keyMap.popitem() #delete
        if item[1] > 1:
            return f"{item[1]}{item[0]}"
        else : return f"{item[0]}"
    return ""

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
# print(solution("a")) TC5
