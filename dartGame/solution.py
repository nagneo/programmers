import re 

def solution(dartResult):
    
    answer = 0
    
    curP = 0
    score = []
    index = 0;
    list = re.split('(\d+)', dartResult)
    for str in list:
        if not str:
            continue
        
        if str.isnumeric():
            curP = int(str)
        else:
            if str == "S":
                curP = curP * 1
            elif str == "S*":
                if len(score) > 0:
                    score[len(score) - 1] += score[len(score) - 1]
                curP = curP * 1 * 2
            elif str == "S#":
                curP = (-1) * 1 * curP
            elif str == "D":
                curP = curP ** 2
            elif str == "D*":
                if len(score) > 0:
                    score[len(score) - 1] += score[len(score) - 1]
                curP = (curP ** 2) * 2
            elif str == "D#":
                curP = (curP ** 2) * (-1)
            elif str == "T":
                curP = curP ** 3
            elif str == "T*":
                if len(score) > 0:
                    score[len(score) - 1] += score[len(score) - 1]
                curP = (curP ** 3) * 2
            elif str == "T#":
                curP = (curP ** 3) * (-1)
                
            score.append(curP)
            index += 1
        
    answer = sum(score)
    return answer
            
# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))