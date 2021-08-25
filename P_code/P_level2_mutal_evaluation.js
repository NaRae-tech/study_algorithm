function grade(s){
  if (s>=90){ return 'A';}
  else if (s>=80 && s<90){ return 'B';}
  else if (s>=70 && s<80){ return 'C';}
  else if (s>=50 && s<70){ return 'D';}
  else {return 'F';}
}
function sum(array){
  var result = 0;
  for (var i =0; i<array.length; i++){
      result+=array[i];
  }
  return result;
}
function solution(scores) {
  var answer = ''
  for (var i=0; i<scores.length; i++){
      var temp = [];
      for (var j=0; j<scores.length; j++){
          temp.push(scores[j][i]);
      }
      var maximum = -1;
      var maximumInd = 0;
      var minimum = 101;
      var minimumInd = 0;
      for (var j = 0;j<temp.length;j++){
          if(maximum<temp[j]){
              maximum = temp[j];
              maximumInd = j;
          }
          else if(maximum===temp[j]){
              maximum = -1;
              maximumInd = 0;
          }
          if(minimum>temp[j]){
              minimum = temp[j];
              minimumInd = j;
          }
          else if(minimum===temp[j]){
              minimum=101;
              minimumInd = 0;
          }
      }
      if (maximum===Math.max.apply(Math, temp) && maximumInd===i){
          answer+=(grade((sum(temp)-maximum)/(temp.length-1)))
      }
      else if (minimum ===Math.min.apply(Math, temp) && minimumInd===i){
          answer+=(grade((sum(temp)-minimum)/(temp.length-1)))
      }
      else{
          answer+=(grade(sum(temp)/temp.length))
      }
  }
  return answer;
}
console.log(solution([[70,49,90],[68,50,38],[73,31,100]]))