function solution(absolutes, signs) {
  var answer = 0;
  absolutes.forEach((num,index) => {
    if (signs[index]) {
      answer += num
    }
    else {
      answer -= num
    }
    
  });

  return answer
}