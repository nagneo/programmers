def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ""
    bufferString = "";
    for ch in s:
        if ch.isnumeric():
           result += convertStringToNum(bufferString, numbers)
           bufferString = ""   
           result += ch
        else:
            bufferString += ch       
    
    result += convertStringToNum(bufferString, numbers)
            
    answer = int(result)
    return answer


def findall(word, str):
    i = str.find(word)
    while i != -1:
        yield i
        i = str.find(word,i+1)
        
def findNumberMap(str, numbers):
    findMap = {}
    for idx, num in enumerate(numbers):
        indexList = [(i, str[i:i+len(num)]) for i in findall(num, str)]
        for index in indexList:
            findMap[index[0]] = idx;
    return findMap   

def convertStringToNum(strNums, numbers):
    result = ""
    if(strNums):
        map = findNumberMap(strNums, numbers)
        sortedMap = sorted(map.items())
        for n in sortedMap:
            result += str(n[1])
            
    return result
    
#solution("one4seveneight")
#solution("23four5six7")
#solution("2three45sixseven")
#solution("123")