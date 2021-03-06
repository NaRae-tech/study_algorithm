package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class B_1927_smallest_heap {

	public static int del(ArrayList<Integer> al) {
		if (al.size()==1) {return 0;}
		else {
			int temp = al.get(1);
			al.set(1,al.get(al.size()-1));
			al.remove(al.size()-1);
			
			int focus= 1;
			while(2*focus<al.size()) {
				int mini = al.get(focus*2);
				int minInd = focus*2;
				if(focus*2+1<al.size() && mini>al.get(focus*2+1)){
					mini = al.get(focus*2+1);
					minInd = focus*2+1;
				}
				if(al.get(focus)<mini) break;
				else {
					int ctemp = al.get(focus);
					al.set(focus, al.get(minInd));
					al.set(minInd, ctemp);
					focus = minInd;
				}
			}
			return temp;
		}
	}
	public static void in(ArrayList<Integer> al, int N) {
		al.add(N);
		int child = al.size()-1;
		int parent = (int)(child/2);
		while(child>0 && al.get(parent)>al.get(child)) {
			int temp = al.get(child);
			al.set(child, al.get(parent));
			al.set(parent, temp);
			child = parent;
			parent = (int)(parent/2);
		}
	}
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int T =0;
		try {T=Integer.parseInt(bf.readLine());} catch(IOException e) {}
		
		ArrayList<Integer> al = new ArrayList<>();
		al.add(0);
		while(T!=0) {
			int N = 0;
			try {N=Integer.parseInt(bf.readLine());} catch(IOException e) {}
			if(N==0) {
				//0또는 가장 작은 수 출력
				System.out.println(del(al));
			}
			else {
				//input
				in(al,N);
			}
			T--;
		}
	}
}
