#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	while (T--) {
		int K = 0, N = 0;
		cin >> K >> N;

		vector<vector<int>>apart(K + 1, vector<int>(N + 1,0));
		for (int i = 0; i <= N; i++) {
			apart[0][i] = i;
		}

		for (int i = 1; i <= K; i++) {
			for (int j = 1; j <= N; j++) {
				apart[i][j] = apart[i - 1][j] + apart[i][j - 1];
			}
		}
		cout << apart[K][N] << "\n";
	}
	return 0;
}