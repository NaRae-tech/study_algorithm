#include <iostream>
#include <vector>
using namespace std;



int main() {
	int N = 0;
	cin >> N;

	vector<int> stair(N);
	int a = 0;
	for (int i = 0; i < N; i++) {
		cin >> a;
		stair[i] = a;
	}

	int distance = N - 1;
	int max = 0;
	while (true) {
		int score = 0;
		int before = 0;
		int now = 1;
		while (true) {
			if (before != 1) {
				//1¹ßÂ¦
			}
			else {
				//2¹ßÂ¦
			}
		}
		if (score > max) {
			max = score; 
		}
	}


	return 0;
}