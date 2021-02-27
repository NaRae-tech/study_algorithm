#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	vector<int> prime;
	if (N > 1) {
		while (N != 1) {
			for (int i = 2; i <= N; i++) {
				if (N % i == 0) {
					prime.push_back(i);
					N = N / i;
					break;
				}
			}
		}
	}

	for (int i = 0; i < prime.size(); i++) {
		cout << prime[i] << endl;
	}

	return 0;
}