#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	vector<long long> num(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	vector<long long> tempNum(N, 0);
	tempNum = num;
	sort(tempNum.begin(), tempNum.end());
	tempNum.erase(unique(tempNum.begin(), tempNum.end()), tempNum.end());

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < tempNum.size(); j++) {
			if (tempNum[j] == num[i]) {
				cout << j << " ";
			}
		}
	}

	return 0;
}