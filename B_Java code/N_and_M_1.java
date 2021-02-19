package baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class N_and_M_1 {
	//0 ~ 8까지 해당 숫자 이미 수열에 포함된 적이 있는지 확인
	static boolean visitedL[] = new boolean[9];
	static int arr[] = new int[9];
	static void function(int index, int N, int M, StringBuilder sR) {
		//수열을 다 채웠을 경우
		if(index == M) {
			for(int i =0;i<M;i++) {
				sR.append(arr[i]+" ");
			}
			sR.append("\n");
			 //하나의 수열 다 출력하면 줄바꾸기
			return;
		}
		else {
			for(int i =1;i<=N;i++) {
				//해당 숫자가 이미 수열 안에 있을 경우
				if(visitedL[i] == true) {
					continue; 
				}
				//해당 숫자가 수열에 없기에 포함시키고 방문했다고 표시
				arr[index] = i;
				visitedL[i] = true;
				//수열을 다채웠으면 출력&다른 수 넣어보기 위해
				//아직 수열을 다 안채웠으면 다음 수를 채우기 위해
				function(index+1, N,M, sR);
				//수열을 다채웠던 수들 출력후 return되어서 여기로 넘어옴
				//다음을 위해 방문 흔적을 지움
				//arr에 처음 들어간 i까지 false로 만든뒤 
				//그 다음 숫자를 arr 첫요소로 넣을 수 있게 i++
				visitedL[i] = false;
			}
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = "";
        StringBuilder sR = new StringBuilder();
        try {
            s = br.readLine();
        } catch (IOException e) {}
        StringTokenizer st = new StringTokenizer(s);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
		function(0,N,M,sR);
		System.out.println(sR);
	}

}
