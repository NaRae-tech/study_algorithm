package programmers;

import java.util.*;
public class Solution_행렬테두리회전하기 {

	public static int[] solution(int rows, int columns, int[][] queries) {
int[] answer = new int[queries.length];
        
        int[][] map = new int[rows][columns];
        for(int i=0; i<rows; i++) {
        	for(int j=0; j<columns; j++) {
        		map[i][j] = i*columns+j+1;
        	}
        }
        
        Deque<Integer> queue = new LinkedList<Integer>();
        
        for(int q=0; q<queries.length; q++) {
            int min = Integer.MAX_VALUE;
            queue.clear();
            
        	int startR = queries[q][0]-1;
        	int startC = queries[q][1]-1;
        	int endR = queries[q][2]-1;
        	int endC = queries[q][3]-1;
        	
        	for(int i=startC; i<endC; i++) {
        		queue.add(map[startR][i]);
        		min = Math.min(min, map[startR][i]);
        	}
        	for(int i=startR; i<endR; i++) {
        		queue.add(map[i][endC]);
        		min = Math.min(min, map[i][endC]);
        	}
        	for(int i=endC; i>startC; i--) {
        		queue.add(map[endR][i]);
        		min = Math.min(min, map[endR][i]);
        	}
        	for(int i=endR; i>startR; i--) {
        		queue.add(map[i][startC]);
        		min = Math.min(min, map[i][startC]);
        	}
        	
        	queue.addFirst(queue.pollLast());
        	answer[q] = min;        	
        	
        	for(int i=startC; i<endC; i++) map[startR][i] = queue.pollFirst();
        	for(int i=startR; i<endR; i++) map[i][endC] = queue.pollFirst();
        	for(int i=endC; i>startC; i--) map[endR][i] = queue.pollFirst();
        	for(int i=endR; i>startR; i--) map[i][startC] = queue.pollFirst();
        }
        return answer;
    }
	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(4,6,new int[][] {{1,1,3,3}})));
	}
}
