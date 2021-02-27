#include <iostream>
using namespace std;

int factorial(int now, int target) {
	if (target > now) {
		return now * factorial(now + 1, target);
	}
	else {
		return now;
	}
}
int main() {
	int N = 0;
	cin >> N;
	if (N == 0) cout << "1\n";
	else cout << factorial(1, N) << endl;
}