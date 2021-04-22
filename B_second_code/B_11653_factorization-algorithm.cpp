#include <iostream>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	int index = 2;
	while (N !=1) {
		if (N%index == 0) {
			cout << index << "\n";
			N /= index;
		}
		else {
			++index;
		}
	}
	return 0;
}