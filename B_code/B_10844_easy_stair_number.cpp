#include <iostream>
#include <vector>
using namespace std;

int mod = 1000000000;

int main() {
	int N = 0;
	cin >> N;

	int result[101][10] = { 0, };
	int answer = 0;

	result[1][0] = 1;
	for (int j = 1; j < 10; j++) {
		result[1][j] = 1;
	}

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0) {
				result[i][j] = (result[i - 1][j + 1]) % mod;
			}
			else if (j == 9) {
				result[i][j] = (result[i - 1][j - 1]) % mod;
			}
			else {
				result[i][j] = (result[i - 1][j - 1] + result[i - 1][j + 1]) % mod;
			}
		}
	}

	for (int j = 1; j < 10; j++) {
		answer += result[N][j];
		answer %= mod;
	}
	
	cout << answer % mod << "\n";
	return 0;
}