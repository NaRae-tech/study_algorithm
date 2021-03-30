#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int N = 0;
	cin >> N;

	vector<int> numbers(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> numbers[i];
	}

	vector<int> sequence;
	for (int i = 0; i < N; i++) {
		if (sequence.empty() || sequence.back() < numbers[i]) {
			sequence.push_back(numbers[i]);
		}
		else {
			vector<int>::iterator iter = lower_bound(sequence.begin(), sequence.end(), numbers[i]);
			*iter = numbers[i];
		}
	}

	cout << sequence.size();
	return 0;
}