#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N = 0;
	int M = 0;
	cin >> N >> M;

	vector<vector<int>> first(N, vector<int>(M));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> first[i][j];
		}
	}
	
	int K = 0;
	cin >> M >> K;
	vector<vector<int>> second(M, vector<int>(K));
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < K; j++) {
			cin >> second[i][j];
		}
	}


	vector<vector<int>> result(N, vector<int>(K));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			int answer = 0;
			for (int a = 0; a < M; a++) {
				answer += first[i][a] * second[a][j];
			}
			result[i][j] = answer;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			cout << result[i][j] << " ";
		}
		cout << "\n";
	}
	return 0;
}