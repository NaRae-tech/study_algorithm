package programmers;

import java.util.*;

public class Solution_단체사진찍기 {
	static boolean[] isSelected;
	static char[] character = new char[] {'A','C','F','J','M','N','R','T'};
	static int[] selected;
	static int answer;
	
	private static boolean check(int n, String[] data, ArrayList<Character>selectedChar) {
		boolean flag = true;
		for(int i=0; i<n; i++) {
			int e1 = selectedChar.indexOf(data[i].charAt(0));
			int e2 = selectedChar.indexOf(data[i].charAt(2));
			int gap = data[i].charAt(4)-'0';
			char sign = data[i].charAt(3);
			switch(sign) {
			case '>':
				if(Math.abs(e1-e2)-1<=gap) flag = false;
				break;
			case '=':
				if(Math.abs(e1-e2)-1!=gap) flag = false;
				break;
			case '<':
				if(Math.abs(e1-e2)-1>=gap) flag = false;
				break;
			}
			if(!flag) break;
		}
		return flag;
	}
	private static void permutation(int cnt, int n, String[] data) {
		if(cnt == 8) {
			ArrayList<Character> selectedChar = new ArrayList<>();
			for(int i=0; i<8; i++) {
				selectedChar.add(character[selected[i]]);
			}
			if(check(n, data, selectedChar)) answer++;
			return;
		}
		for(int i=0; i<8; i++) {
			if(isSelected[i]) continue;
			isSelected[i] = true;
			selected[cnt] = i;
			permutation(cnt+1,n,data);
			isSelected[i] = false;
		}
	}
	public static int solution(int n, String[] data) {
        answer = 0;
        isSelected = new boolean[8];
        selected = new int[8];
        permutation(0,n,data);
        
        return answer;
    }
	 
	public static void main(String[] args) {
		int n = 2;
		//A어피치 C콘 F프로도 J제이지 M무지 N네오 R라이언 T튜브
		String[] data = new String[] {"M~C<2", "C~M>1"};
		System.out.println(solution(n,data));
	}

}
