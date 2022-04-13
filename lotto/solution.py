def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    
    hit_cnt = 0;
    unknown_cnt = 0;
    for num in lottos:
        if num in win_nums:
            hit_cnt += 1
        if num == 0:
            unknown_cnt += 1
    
    max_cnt = hit_cnt + unknown_cnt;
    min_cnt = hit_cnt
    
    answer = [rank[max_cnt], rank[min_cnt]]    
    return answer;