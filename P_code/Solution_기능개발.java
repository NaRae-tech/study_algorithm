package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_기능개발 {

	public static int[] solution2(int[] progresses, int[] speeds) {       
        int[] days = new int[progresses.length];
        for(int i=0; i<days.length; i++) {
        	days[i] = (int) Math.ceil(1.0*((100-progresses[i]))/speeds[i]);
        }
        
        int count = 1;
        int target = days[0];
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i=1; i<days.length; i++) {
        	if(target>=days[i]) count++;
        	else {
        		temp.add(count);
        		count =1;
        		target = days[i];
        	}
        }
        temp.add(count);
        
        int[] answer = new int[temp.size()];
        for(int i=0; i<temp.size(); i++) {
        	answer[i] = temp.get(i);
        }
        
        return answer;
    }
	public static int[] solution(int[] progresses, int[] speeds) {
		Queue<Integer> days = new LinkedList<Integer>();
		for(int i=0; i<progresses.length; i++) {
        	days.add((int)Math.ceil(1.0*((100-progresses[i]))/speeds[i]));
        }
		
		Queue<Integer> temp = new LinkedList<Integer>();
		int count = 0;
		int target = days.peek();
		while(!days.isEmpty()) {
			int now = days.poll();
			if(target>=now) count++;
			else {
				temp.add(count);
				count = 1;
				target = now;
			}
		}
		temp.add(count);
		
		int[] answer = new int[temp.size()];
		int index = 0;
        while(!temp.isEmpty()) {
        	answer[index++] = temp.poll();
        }
        
		return answer;
	}
	
	public static void main(String[] args) {
		int[] progresses = new int[] {95,90,99,99,80,99};
		int[] speeds = new int[] {1,1,1,1,1,1};
		
		System.out.println(Arrays.toString(solution(progresses, speeds)));
	}

}
