// 프로그래머스 
// 키패드 누르기
// https://school.programmers.co.kr/learn/courses/30/lessons/67256

function solution(numbers, hand) {
  let answer = ''
    
  //dictionary 
  const keypadMap = {
      1:[0,0], 2:[0,1], 3:[0,2],
      4:[1,0], 5:[1,1], 6:[1,2],
      7:[2,0], 8:[2,1], 9:[2,2],
      '*':[3,0], 0:[3,1], '#':[3,2],
  }

  //init
  let leftPos = keypadMap['*']
  let rightPos = keypadMap['#']

  //list - 키패드 위치 0:C(중앙), [1,4,7]:L(좌) [3,6,9]:R(우)
  const hands = ['C','L','C','R','L','C','R','L','C','R']

  for (var n of numbers) {
    const keyPos = keypadMap[n]
    if (hands[n] == 'C') {
      //compute
      const leftDist = Math.abs(keyPos[0] - leftPos[0]) + Math.abs(keyPos[1] - leftPos[1])
      const rightDist = Math.abs(keyPos[0] - rightPos[0]) + Math.abs(keyPos[1] - rightPos[1])
      if (leftDist == rightDist){
          if (hand == "right"){
              rightPos = keyPos
              answer += "R"
          } else{
            leftPos = keyPos
            answer += "L"
          }
      } else if (leftDist < rightDist){
        answer += "L"
        leftPos = keyPos
      } else{
        answer += "R"
        rightPos = keyPos
      }
    }else {
      answer += hands[n]
      if (hands[n] === "L") {
        leftPos = keyPos
      }
      else {
        rightPos = keyPos
      }
    }
  }

  return answer
}

// 기댓값 "LRLLLRLLRRL"
console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))