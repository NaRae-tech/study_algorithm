function solution(table, languages, preference) {
  var answer='';
  var result = {};
  table.forEach(row => {
    const [occupation, ...ranks] = row.split(' ');
    var current = 0;
    /*호감도 체크 */
    for (var j=0; j<languages.length;j++){
      const rank = ranks.findIndex(l=>l===languages[j]);
      if (rank === -1) continue;
      current += (preference[j]*(ranks.length-rank))
    }
    result[occupation] = current;
  });
  result = Object.keys(result).sort().reduce((r, k) => (r[k] = result[k], r), {});
  var answer = Object.keys(result).reduce((a,b)=> result[a]>=result[b]? a:b);
  return answer;
}

var t = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
var lang = ["JAVA", "JAVASCRIPT"]
var pre =[7,5]
console.log(solution(t,lang,pre))