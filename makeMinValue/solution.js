function solution(A,B){
  let answer = BigInt(0);

  A.sort((a, b) => b - a)
  // 숫자 정렬. 기본값은 유니코드 정렬
  B.sort((a, b)=> a - b)

  const zip = (a, b) => a.map((k, i) => [k, b[i]]);
  for (const [a, b] of zip(A, B)) {
    answer += BigInt(a * b)
  }

  return answer;
}