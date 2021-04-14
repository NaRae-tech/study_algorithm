#include <iostream>
using namespace std;

int main() {

	int N = 0;
	cin >> N;

	int sum = 1;
	int level = 1;

	while (true) {
		if (sum >= N) break;
		++level;
		sum += level;
	}

	int gap = sum - N;
	if (level % 2 == 0) {
		cout << level - gap << "/" << 1 + gap;
	}
	else {
		cout << 1 + gap << "/" << level - gap;
	}
	return 0;
}