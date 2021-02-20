#include <iostream>
using namespace std;

int main() {
	int N = 0;
	int M = 0;
	cin >> N >> M;

	int minList[100];
	for (int i = 0; i < N; i++) {
		int min = 10001;
		int a = 0;
		for (int j = 0; j < M; j++) {
			cin >> a;
			if (a <= min) {
				min = a;
			}
		}
		minList[i] = min;
	}
	int max = -1;
	for (int i = 0; i < N; i++) {
		if (minList[i] >= max) {
			max = minList[i];
		}
	}
	cout << max;

}