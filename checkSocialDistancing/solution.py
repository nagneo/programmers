def solution(places):
    
    answer = []
    for waitingRoom in places:
        isFail = False;
        for x, row in enumerate(waitingRoom):
            for y, seat in enumerate(row):
                #print(x,y, seat)
                if seat != 'P':
                    continue
                
                points = getPointsToCheck(x,y)
                for p in points:
                    if waitingRoom[p[0]][p[1]] == 'X':
                        continue
                    
                    #manhatten
                    manhattenDistPoints = getPointsToCheck(p[0],p[1])
                    for distP in manhattenDistPoints:
                        if distP == (x,y):
                            continue
                        
                        if waitingRoom[distP[0]][distP[1]] == 'P':
                            isFail = True;
                            break;
                    if isFail:
                        break;
                if isFail:
                    break;
            if isFail:
                break;
        if isFail:
            answer.append(0)
        else: answer.append(1)
        
    return answer
                    
def getPointsToCheck(x,y):
    result = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
        p = (x + dir[0], y + dir[1])
        if p[0] in range(0,5) and p[1] in range(0,5):
            result.append(p)

    return result


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))