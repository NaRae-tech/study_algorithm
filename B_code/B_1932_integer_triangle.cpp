#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	vector<vector<int>> triangle(N, vector<int>(N));
	int a = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j <= i; j++) {
			cin >> a;
			triangle[i][j] = a;
		}
	}
	
	int max = 0;
	for (int i = 1; i < N; i++) {
		for (int j = 0; j <= i;j++) {
			if (j == 0) {
				triangle[i][j] += triangle[i - 1][0];
			}
			else if (j == i) {
				triangle[i][j] += triangle[i - 1][j - 1];
			}
			else {
				triangle[i][j] += ((triangle[i - 1][j - 1] >= triangle[i - 1][j]) ? triangle[i - 1][j - 1] : triangle[i - 1][j]);
			}
			if (max <= triangle[i][j]) max = triangle[i][j];
		}
	}

	cout << max << "\n";
	
	return 0;
}