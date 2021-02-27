#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int N = 0;
	cin >> N;
	vector<int>numbers;
	for (int i = 0; i < N; i++) {
		int n = 0;
		cin >> n;
		numbers.push_back(n);
	}
	sort(numbers.begin(), numbers.end());
	cout << numbers[0] * numbers[int(numbers.size() - 1)];
	return 0;
}