function solution(expression) {
  var answer = 0;
  var priority = [["*","+","-"], ["*","-","+"],["+","*","-"], ["-","*","+"],["+","-","*"], ["-","+","*"]]
  
  // priority.forEach(element => {
  //   console.log(element)
  // });

  var nodes = expression.slit("*")
  console.log(nodes)
}

function split(expression) {
  let result = 0
  expression.split().forEach(ch => {
    if (isNaN(ch)) {
      
    }
    
  });
}

solution("100-200*300-500+20")