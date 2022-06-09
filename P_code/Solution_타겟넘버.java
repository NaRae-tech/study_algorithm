package programmers;

import java.util.Arrays;

public class Solution_타겟넘버 {
	
	static boolean[] checked;
	static int[] num;
	static int T;
	static int how;
	private static void subset(int cnt, int N) {
		if(cnt==N) {			
			int sum = 0;
			for(int i=0; i<N; i++) {
				if(checked[i]) sum+=num[i];
				else sum-=num[i];
			}
			if(sum == T) how++;
			
			return;
		}
		checked[cnt] = true;
		subset(cnt+1, N);
		checked[cnt] = false;
		subset(cnt+1, N);
	}
	public static int solution(int[] numbers, int target) {
        num = numbers;
        T = target;
        how = 0;
        checked = new boolean[numbers.length];
        subset(0, numbers.length);
        
        return how;
    }
	public static void main(String[] args) {
		int[] numbers = new int[] {4,1,2,1};
		int target = 4;
		
		System.out.println(solution(numbers,target));
	}

}
