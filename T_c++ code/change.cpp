#include <iostream>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	int count = 0;
	while (N != 0) {
		if (N >= 500) {
			++count;
			N -= 500;
		}
		else if (N < 500 && N >= 100) {
			++count;
			N -= 100;
		}
		else if (N < 100 && N >= 50) {
			++count;
			N -= 50;
		}
		else {
			++count;
			N -= 10;
		}
	}
	cout << count;
	return 0;
}