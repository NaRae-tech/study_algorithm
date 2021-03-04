package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class B_9461_sequence {
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		try {s=bf.readLine();}catch(IOException e) {}
		int T = Integer.parseInt(s);
		
		while(T!=0) {
			try {s=bf.readLine();}catch(IOException e) {}
			int N = Integer.parseInt(s);
			ArrayList<Long> list = new <Long> ArrayList();
			list.add(0, (long)0);
			list.add(1, (long)1);
			list.add(2, (long)1);
			list.add(3, (long)1);
			list.add(4, (long)2);
			for(int i =5;i<=N;i++) {
				list.add(i, (long)(list.get(i-1)+list.get(i-5)));
			}
			System.out.println(list.get(N));
			--T;
		}
	}

}
