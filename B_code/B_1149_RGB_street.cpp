#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;
	
	int price[1001][3] = { 0, };
	for (int i = 0; i < N; i++) {
		cin >> price[i][0] >> price[i][1] >> price[i][2];
	}

	int dq[1001][3] = { 0, };
	for (int i = 1; i <= N; i++) {
		dq[i][0] = price[i - 1][0] + min(dq[i - 1][1], dq[i - 1][2]);
		dq[i][1] = price[i - 1][1] + min(dq[i - 1][0], dq[i - 1][2]);
		dq[i][2] = price[i - 1][2] + min(dq[i - 1][0], dq[i - 1][1]);
	}

	cout << min(dq[N][0], min(dq[N][1], dq[N][2])) << "\n";
	return 0;
}