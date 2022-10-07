function solution(a, b) {

  var answer = 0;
  a.forEach((element, idx) => {
    answer += element * b[idx]
  });


  return answer;
}