def solution(participant, completion):
    hashMap = {}
    sum = 0 
    
    for part in participant: 
        hashMap[hash(part)] = part 
        sum += hash(part) 
    
    for comp in completion: 
        sum -= hash(comp) 
    
    return hashMap[sum]