package programmers;

public class Solution_124나라의숫자 {

	public static String solution(int n) {
		String[] character = new String[] {"4","1","2"};
        String answer = "";
        while(n>0) {
        	answer = character[n%3]+answer;
        	if(n%3==0) n=n/3-1;
        	else n/=3;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		System.out.println(solution(9));
	}

}
