#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int M = 0;
	int N = 0;
	cin >> M >> N;

	int cnt = 0;
	int sum = 0;
	int minimum = N;
	for (int i = M; i <= N; i++) {
		bool primeFlag = true;
		if (i == 1) { primeFlag = false; }
		for (int j = 2; j < i; j++) {
			if (i%j == 0) { primeFlag = false; }
		}
		if (primeFlag) {
			++cnt;
			sum += i;
			minimum = min(minimum, i);
		}
	}
	if (cnt == 0) { cout << -1; }
	else {
		cout << sum << "\n" << minimum;
	}
	
	return 0;
}