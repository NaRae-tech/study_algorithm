#include <iostream>
using namespace std;

int fibonacci(int now) {
	if (now > 1) {
		return fibonacci(now - 1) + fibonacci(now - 2);
	}
	else if (now == 1) {
		return 1;
	}
	else if (now == 0) {
		return 0;
	}
}
int main() {
	int N = 0;
	cin >> N;
	
	 cout << fibonacci(N) << "\n";
}