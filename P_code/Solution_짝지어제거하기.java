package programmers;

import java.util.Stack;
public class Solution_짝지어제거하기 {

	public static int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length(); i++) {
        	if(stack.isEmpty()) stack.push(s.charAt(i));
        	else {
        		if(stack.peek()==s.charAt(i)) stack.pop();
        		else stack.push(s.charAt(i));
        	}
        }

        return stack.isEmpty()?1:0;
    }
	public static void main(String[] args) {
		System.out.println(solution("cdcd"));
	}

}
