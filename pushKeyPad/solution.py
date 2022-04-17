def solution(numbers, hand):
    answer = ''
    
    #dict 
    keypadMap = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2),
    }
    
    #init
    leftPos = keypadMap['*']
    rightPos = keypadMap['#']
    
    #list
    hands = ['C','L','C','R','L','C','R','L','C','R']
    
    for n in numbers:
        keyPos = keypadMap[n]
        if hands[n] == 'C':
            #compute
            leftDist = abs(keyPos[0] - leftPos[0]) + abs(keyPos[1] - leftPos[1])
            rightDist = abs(keyPos[0] - rightPos[0]) + abs(keyPos[1] - rightPos[1])
            if leftDist == rightDist:
                if hand == "right":
                    rightPos = keyPos
                    answer += "R"
                else:
                    leftPos = keyPos
                    answer += "L"
            elif leftDist < rightDist:
                answer += "L"
                leftPos = keyPos
            else:
                answer += "R"
                rightPos = keyPos
        else:
            answer += hands[n]
            if hands[n] == "L":
                leftPos = keyPos
            else:
                rightPos = keyPos

    return answer

#print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
#print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))