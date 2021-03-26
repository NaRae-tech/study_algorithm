#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int make(vector<long long> L, long long length) {
	int total = 0;
	for (int i = 0; i < L.size(); i++) {
		total += floor(L[i] / length);
	}
	return total;
}
int main() {
	int N = 0;
	int K = 0;
	cin >> N >> K;

	vector<long long > LAN(N, 0);
	long long L = 0;
	long long maximum = 0;
	for (int i = 0; i < N; i++) {
		cin >> L;
		LAN[i] = L;
		maximum = max(maximum, L);
	}

	long long maxi = maximum;
	long long mini = 1;
	long long middle = 0;
	int result = 0;
	int cnt = 0;
	while (mini<=maxi) {
		middle = ceil((maxi + mini) / 2);
		cnt = make(LAN, middle);
		if (cnt >= K) {
			result = (result < middle) ? middle : result;
			mini = middle+1;
		}
		else {
			maxi = middle-1;
		}
	}
	cout << result;
	

	return 0;
}