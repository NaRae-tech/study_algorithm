package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class fibonacci_dynamic{
	static int arr[] = new int[41];
	public static int fibonacci(int n) {
		if(n==0) {
			arr[n] = 0;
			return 0;
		}
		else if(n==1) {
			arr[n] = 1;
			return 1;
		}
		if(arr[n]!=0) {return arr[n];}
		else {
			return arr[n] = fibonacci(n-1)+fibonacci(n-2);
		}
	}
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		try {
			int N = Integer.parseInt(bf.readLine());
			for(int i=0;i<N;i++) {
				try {
					int A = Integer.parseInt(bf.readLine());
					if(A==0) {
						sb.append("1"+" "+"0"+"\n");
					}
					else if(A==1) {
						sb.append("0"+" "+"1"+"\n");
					}
					else{
						fibonacci(A);
						sb.append(arr[A-1]+" "+arr[A]+"\n");
					}
					
				}catch(IOException e) {}
			}
			System.out.println(sb);
		}catch(IOException e) {}
	}
}