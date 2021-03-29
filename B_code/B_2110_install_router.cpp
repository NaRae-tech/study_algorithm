#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool point(vector<int> home, int C, int middle) {
	int cnt = 1;
	int before = home[0];
	for (int i = 1; i < home.size(); i++) {
		if (home[i] - before >= middle) {
			cnt += 1;
			before = home[i];
		}
	}
	if (cnt >= C) {
		return true;
	}
	return false;
}
int main() {
	int N = 0;
	int C = 0;
	cin >> N >> C;

	vector<int>home(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> home[i];
	}
	sort(home.begin(), home.end());

	int left = 1;
	int right = home[N - 1] - home[0];
	int middle = 0;
	int result = 0;
	while (left <= right) {
		middle = (left + right) / 2;
		if (point(home, C, middle)) {
			result = max(result, middle);
			left = middle + 1;
		}
		else {
			right = middle - 1;
		}
	}

	cout << result;

	return 0;
}