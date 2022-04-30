def solution(record):
    answer = []
    
    idNicknameMap = {}
    inOutList = []
    for str in record:
        strs = str.split()
        id = strs[1]
        if strs[0] == 'Enter' or strs[0] == 'Change':
            idNicknameMap[id] = strs[2] #add or update
            if strs[0] == 'Enter':
                inOutList.append((id, '님이 들어왔습니다.'))
        elif strs[0] == 'Leave':
            inOutList.append((id, '님이 나갔습니다.'))     
    answer = [ f"{idNicknameMap[id]}{str}" for id, str in inOutList]
    return answer

#print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))