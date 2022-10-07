function solution(numbers) {
  const answer = [...Array(10).keys()].reduce((acc, cur) => acc + cur) 
          - numbers.reduce((acc, cur) => acc + cur)

  return answer;
}