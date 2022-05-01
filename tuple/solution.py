def solution(s):
    
    answer = []
    # 개수대로 정렬
    s = s[2:-2]
    array = s.split('},{')
    array.sort(key = len)
    for setStr in array:
        sets = setStr.split(',')
        for s in sets:
            num = int(s)
            if num not in answer:
                answer.append(int(s))
    
    return list(answer)

#print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))