#include <iostream>
using namespace std;
int main() {
	int N = -1;
	while(true) {
		cin >> N;
		if (N == 0) break;

		bool primeCheck[246913] = { };
		primeCheck[0] = false;
		primeCheck[1] = false;
		for (int i = 2; i <= 2 * N; i++) {
			primeCheck[i] = true;
		}

		for (int i = 2; i <= 2 * N; i++) {
			if (primeCheck[i]) {
				for (unsigned long long int j = 2 * i; j <= 2 * N; j += i) {
					primeCheck[j] = false;
				}
			}
		}

		int count = 0;
		for (int i = N + 1; i <= 2 * N; i++) {
			if (primeCheck[i]) {
				count++;
				//cout << i << " ";
			}
		}
		cout << count << "\n";
	}
	return 0;
}


/* 시간초과
		int count = 0;
		for (int i = N + 1; i <= 2 * N; i++) {
			bool flag = true;
			for (int j = 2; j < i; j++) {
				if (i%j == 0) {
					flag = false;
					break;
				}
			}
			if (flag) count++;
		}
		cout << count << "\n";
*/