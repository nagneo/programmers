def solution(board, moves):
    answer = 0
    reverse = []
    basket = []
    rowLen = len(board);
    for i in range(rowLen):
        column = getColumn(board, i)
        reverse.append(column)
    
    for col in moves:
        item = getItem(reverse[col - 1])
        if item is not 0:
            basket.append(item)
            while IsDuplicated(basket):
                answer += 2
                basket.pop()
                basket.pop()
    
    return answer

def getColumn(matrix, i):
    return [row[i] for row in matrix]

def getItem(list):
    if len(list) == 0:
        return 0
    
    item = list.pop(0)
    while(item == 0):
        if len(list) == 0:
            return 0
        item = list.pop(0)
    return item

def IsDuplicated(list):
    if len(list) < 2:
        return False
    else:
        return list[-1] == list[-2]

#print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))