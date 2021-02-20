#include <iostream>
using namespace std;

int main() {
	int N = 0;
	int K = 0;
	cin >> N >> K;

	int result = 0;
	while (true) {
		int target = int(N / K)*K;
		result += (N - target);
		N = target;

		if (N < K)  break;
		result += 1;
		N /= K;
	}

	result += (N - 1);
	cout << result;
	return 0;
}