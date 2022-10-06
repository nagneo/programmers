// 숫자의 표현
// 힌트: 시그마 연산 식을 세워 풀기
function solution(n) {
  let startN = 1
  let count = 1 
  let answer = 0
  while (startN >= 1) {
    startN = tryGetStartInt(n, count)
    // 정수로 나누어 떨어지는지 확인 
    if (startN >= 1 && parseInt(startN) === startN) {
      answer += 1
    }
    count += 1
  }

  return answer
}


function tryGetStartInt(n, count) {
  return (n - [...Array(count).keys()].reduce((a,b) => a+b, 0)) / count
}