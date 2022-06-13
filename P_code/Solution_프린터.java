package programmers;

import java.util.*;
public class Solution_프린터 {

	public static int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<int[]> queue = new LinkedList<int[]>();
        for(int i=0; i<priorities.length; i++) {
        	queue.add(new int[] {priorities[i], i});
        }
        
        int print = 0;
        while(true) {
        	int length = queue.size();
        	int max = 0;
        	for(int i=0; i<length; i++) {
        		int[] temp = queue.poll();
        		max = Math.max(max, temp[0]);
        		queue.add(temp);
        	}
        	
        	int[] now = queue.poll();
        	if(max==now[0]) {
        		print++;
        		if(now[1]==location) {
        			answer = print;
        			break;
        		}
        	}
        	else {
        		queue.add(now);
        	}
        	
        }
        return answer;
    }
	public static void main(String[] args) {
		int[] priorities = new int[] {1,1,9,1,1,1};
		int location = 0;
		System.out.println(solution(priorities, location));
	}

}
