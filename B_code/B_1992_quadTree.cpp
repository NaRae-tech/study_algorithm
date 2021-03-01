#include<iostream>
#include<string>
#include<vector>
using namespace std;

string answer = "";
void quadTree(vector<vector<int>> &input, int X, int Y, int size) {
	bool isCombine = true;
	int begin = input[X][Y];
	for (int j = Y; j < Y + size; j++) {
		for (int i = X; i < X + size; i++) {
			if (begin != input[i][j]) {
				isCombine = false;
				break;
			}
		}
		if (isCombine == false) break;
	}

	if (isCombine) {
		answer.append(to_string(begin));
		return;
	}

	size = (int)(size / 2);
	answer.append("(");
	quadTree(input, X, Y, size);
	quadTree(input, X, Y + size, size);
	quadTree(input, X + size, Y, size);
	quadTree(input, X + size, Y + size, size);
	answer.append(")");
}
int main() {
	int N = 0;
	cin >> N;
	cin.ignore();
	vector<vector<int>> input(N,vector<int>(N));
	for (int i = 0; i < N; i++) {
		string temp = "";
		getline(cin, temp);
		for (int j = 0; j < N; j++) {
			input[i][j] = temp[j]-'0';
		}
	}
	quadTree(input, 0, 0, N);
	cout << answer;

	return 0;
}