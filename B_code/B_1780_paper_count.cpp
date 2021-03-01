#include<iostream>
#include<vector>
#include<string>
using namespace std;
vector<int> answer;
void quadTreeVer2(vector<vector<int>> &p, int x, int y, int size) {
	bool isCombine = true;
	int begin = p[x][y];
	for (int j = y; j < y + size; j++) {
		for (int i = x; i < x + size; i++) {
			if (p[i][j] != begin) {
				isCombine = false;
				break;
			}
		}
		if (!isCombine) break;
	}

	if (isCombine) {
		answer.push_back(begin);
		return;;
	}

	size = (int)(size / 3);
	quadTreeVer2(p, x, y, size);
	quadTreeVer2(p, x+size, y, size);
	quadTreeVer2(p, x+2*size, y, size);

	quadTreeVer2(p, x, y+size, size);
	quadTreeVer2(p, x + size, y + size, size);
	quadTreeVer2(p, x + 2 * size, y + size, size);

	quadTreeVer2(p, x, y + 2*size, size);
	quadTreeVer2(p, x + size, y + 2 * size, size);
	quadTreeVer2(p, x + 2 * size, y + 2 * size, size);
}
int main() {
	int N = 0;
	cin >> N;

	vector<vector<int>> paper(N, vector<int>(N));
	int a = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> a;
			paper[i][j] = a;
		}
	}

	quadTreeVer2(paper, 0, 0, N);

	int minus = 0;
	int zero = 0;
	int plus = 0;
	for (int i = 0; i < answer.size(); i++) {
		if (answer[i] == -1)++minus;
		else if (answer[i] == 0) ++zero;
		else if (answer[i] == 1) ++plus;
	}
	cout << minus << "\n" << zero << "\n" << plus;
	return 0;
}