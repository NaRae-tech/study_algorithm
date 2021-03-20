#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	int K = 0;
	cin >> N >> K;

	vector<int> weight;
	vector<int> value;
	int w = 0;
	int v = 0;
	for (int i = 0; i < N; i++) {
		cin >> w >> v;
		weight.push_back(w);
		value.push_back(v);
	}

	vector<vector<int>> dq(N + 1, vector<int>(K + 1));
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= K; j++) {
			if (i == 0 || j == 0) dq[i][j] = 0;
			else if (weight[i - 1] <= j) {
				dq[i][j] = max(dq[i - 1][j], (value[i - 1] + dq[i-1][j - weight[i - 1]]));
 			}
			else dq[i][j] = dq[i - 1][j];
		}
	}

	cout << dq[N][K];
	return 0;
}