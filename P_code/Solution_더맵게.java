package programmers;

import java.util.*;
public class Solution_더맵게 {
	public static int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for(long s : scoville) pq.add(s);
        
        while(pq.peek()<K) {
        	answer++;
        	long e1 = pq.poll();
        	if(pq.size()==0) {
        		answer = -1;
        		break;
        	}
        	long e2 = pq.poll();
        	pq.add(e1+e2*2);
        }
        
        return answer;
    }
	public static void main(String[] args) {
		int[] scoville = new int[] {1, 2, 3, 9, 10, 12};
		int K = 7;
		System.out.println(solution(scoville, K));
	}

}
