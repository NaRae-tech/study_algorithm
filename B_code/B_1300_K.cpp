#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

//파라미터의 수보다 작은 수의 개수 return
int cntSmaller(long long N, long long m) {
	int total = 0;
	for (int i = 1; i <= N; i++) {
		total += min(N, m / i);
	}
	return total;
}
int main() {
	long long  N = 0;
	long long K = 0;
	cin >> N >> K;

	long long left = 1;
	long long right = K;
	long long middle = 0;
	long long result = 0;
	int cnt = 0;
	while (left <= right) {
		middle = (left + right) / 2;
		cnt = cntSmaller(N, middle);
		 if (cnt >= K) {
			right = middle - 1;
			result = middle;
		}
		else{
			left = middle + 1;
		}
	}

	cout << result;
	return 0;
}