#include<iostream>
#include<vector>
#include<string>
using namespace std;
string answer = "";

void quadTree(vector<vector<int>> &p, int X, int Y, int size) {
	bool iscombine = true;
	int begin = p[X][Y];
	for (int y = Y; y < Y + size; y++) {
		for (int x = X; x < X + size; x++) {
			if (begin != p[x][y]) {
				iscombine = false;
				break;
			}
		}
		if (iscombine == false) break;
	}

	if (iscombine) {
		answer.append(to_string(begin));
		return;
	}

	size = int(size / 2);
	answer.append("(");
	quadTree(p, X, Y, size);
	quadTree(p, X + size, Y, size);
	quadTree(p, X, Y + size, size);
	quadTree(p, X + size, Y + size, size);
	answer.append(")");
}
int main() {
	int N = 0;
	cin >> N;
	
	vector<vector<int>> paper(N + 1, vector<int>(N + 1));
	int input = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> input;
			paper[i][j] = input;
		}
	}

	quadTree(paper, 0, 0, N);

	int white = 0;
	int blue = 0;
	for (unsigned int i = 0; i < answer.size(); i++) {
		if (answer[i] == '(' || answer[i] == ')')
			continue;
		else if (answer[i] == '1') ++blue;
		else if (answer[i] == '0')++white;
	}
	cout << white << "\n" << blue;
	return 0;
}