def solution(sizes):
    return max([max(i) for i in sizes]) * max([min(i) for i in sizes])

#print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
#print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
#print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# def solution2(sizes):
    
#     maxW = 0
#     maxH = 0
#     for size in sizes:
#         size.sort()
#         if size[0] > maxW:
#             maxW = size[0]
#         if size[1] > maxH:
#             maxH = size[1]
        
#     return maxW * maxH