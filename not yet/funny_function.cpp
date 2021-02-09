#include <iostream>
using namespace std;

int funnyFunction(int a, int b, int c) {
	if ((a == 0) || (b == 0) || (c == 0)) { return 1; }
	else if ((a > 20) || (b > 20) || (c > 20)) { return funnyFunction(20, 20, 20); }
	else if ((a < b) && (b < c)) { return funnyFunction(a, b, c - 1) + funnyFunction(a, b - 1, c - 1) - funnyFunction(a, b - 1, c); }
	else {
		return funnyFunction(a - 1, b, c) + funnyFunction(a - 1, b - 1, c) + funnyFunction(a - 1, b, c - 1) - funnyFunction(a - 1, b - 1, c - 1);
	}
}
int main() {
	
	int a = 0;
	int b = 0;
	int c = 0;
	while (true) {
		cin >> a >> b >> c;
		if ((a == -1) && (b == -1) && (c == -1)) { break; }
		int answer = funnyFunction(a, b, c);
		cout << "w(" << a << ", " << b << ", " << c << ") = " << answer << "\n";
	}
	return 0;
}