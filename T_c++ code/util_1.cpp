#include <iostream>
using namespace std;

int main() {
	int N = 0;
	int K = 0;
	cin >> N >> K;

	int count = 0;
	while (N != 1) {
		if (N >= K && N%K==0) {
			++count;
			N /= K;
		}
		else {
			++count;
			N -= 1;
		}
	}
	cout << count;
	return 0;
}