function solution(answers) {
  let answer = []
  const order1 = [1,2,3,4,5]
  const order2 = [2,1,2,3,2,4,2,5]
  const order3 = [3,3,1,1,2,2,4,4,5,5]

  surrenderMap = {1:0, 2:0, 3:0}

  answers.forEach((ans, i) => {
    if (ans === order1[i % order1.length]){
      surrenderMap[1] += 1
    }
    if (ans === order2[i % order2.length]){
      surrenderMap[2] += 1
    }
    if (ans === order3[i % order3.length]){
      surrenderMap[3] += 1
    }
  });
  
  let max = 0;
  let isChanged = false;
  for (const key in surrenderMap) {
    if (surrenderMap[key] > max) {
      max = surrenderMap[key]
      isChanged = true;
    }
    if (max === surrenderMap[key]) {
      if(isChanged && answer.length > 0) {
        // 이전 최댓값 제거
        answer.pop()
      }
      isChanged = false;
      answer.push(parseInt(key))
    }
  }

  return answer.sort()
}


console.log(solution([1,2,3,4,5]));