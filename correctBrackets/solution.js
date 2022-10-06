function solution(s){
  let bracket = []
  
  // 효율성 1번 - 테스트 케이스 
  if (s[0]===')') {
    return false
  }
  for (const ch of s) {
    if (ch === "(") {
      bracket.push(ch)
    }
    else if(ch === ")") {
      if (!bracket) {
        return false
      }
      const popped = bracket.pop()
      if (popped !== "(") {
        return false
      }
      
    }
  }

  return bracket.length === 0 
}