#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	vector<int> arr = { 1, 5, 2, 6, 3, 7, 4 };
	vector<vector<int>> commands = { {2, 5, 3},{4, 4, 1},{1, 7, 3}};

	vector<int> answer;
	for (int a = 0; a < commands.size(); a++) {
		int i = commands[a][0]-1;
		int j = commands[a][1]-1;
		int k = commands[a][2]-1;

		vector<int>temp;
		for (int b = i; b <= j; b++) {
			temp.push_back(arr[b]);
		}
		sort(temp.begin(), temp.end());
		answer.push_back(temp[k]);
	}
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i];
	}

	return 0;
}