#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int N = 0;
	int M = 0;
	int K = 0;
	cin >> N >> M >> K;

	vector<int>numbers;
	for (int i = 0; i < N;i++) {
		int a = 0;
		cin >> a;
		numbers.push_back(a);
	}
	sort(numbers.begin(), numbers.end(),greater<int>());

	int result = 0;
	int count = 0;
	int index = 0;
	while (M--) {
		if (count == 3)  {
			result += numbers[index + 1];
			count = 0;
		}
		else {
			result += numbers[index];
			++count;
		}
	}
	cout << result;
	return 0;
}