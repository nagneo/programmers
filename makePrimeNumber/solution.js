// 프로그래머스
// 소수 만들기
// https://programmers.co.kr/learn/courses/30/lessons/12977


function solution(nums) {
  var answer = 0;
  const list = getCombinations(nums, 3);
  for (var set of list) {
    // summation 
    const s = set.reduce((a, b) => a + b, 0);
    let isPrime = true;
    for (var i = 2; i < s; i++ ) {
      if (s % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      answer += 1;
    }
  }

  return answer;
}

function getCombinations (arr, selectNumber) {
  // 재귀함수 종료 조건 
  if (selectNumber === 1) {
    return arr.map((value) => [value]);
  }
  
  const results = [];
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombinations(rest, selectNumber - 1); // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((combination) => [fixed, ...combination]); //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached); // 배열 spread syntax 로 모두다 push
  });

  return results;
}

//console.log(solution([1,2,3,4]))
console.log(solution([1,2,7,6,4]))