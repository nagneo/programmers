function solution(lottos, win_nums) {
  let answer = [];
  const rank = [6,6,5,4,3,2,1]

  let hit_cnt = 0;
  let unknown_cnt = 0;
  lottos.forEach(num => {
    if (win_nums.includes(num)) {
      hit_cnt += 1
    }
    if (num === 0) {
      unknown_cnt += 1
    }
  });

  const max_cnt = hit_cnt + unknown_cnt;
  const min_cnt = hit_cnt;

  answer = [rank[max_cnt], rank[min_cnt]]
  return answer;
}

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])