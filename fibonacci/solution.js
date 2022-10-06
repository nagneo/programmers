function solution(n) {
  return fibonacci(n) % BigInt(1234567)
}

function fibonacci(n) {
  let ppre = BigInt(0)
  let pre = BigInt(1)
  let answer = BigInt(0)
  for (const i of Array(n-1).keys()) {
    answer = ppre + pre
    
    //set for next
    ppre = pre
    pre = answer
  }

  return answer
}