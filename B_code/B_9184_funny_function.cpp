#include <iostream>
using namespace std;

int d[21][21][21];
int w(int a, int b, int c) {
	if ((a <= 0) || (b <= 0) || (c <= 0)) return 1;
	else if ((a > 20) || (b > 20) || (c > 20)) return w(20, 20, 20);
	else if ((a < b) && (b < c)) {
		if (d[a][b][c] != 0) return d[a][b][c];
		return d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
	}
	else {
		if (d[a][b][c] != 0) return d[a][b][c];
		return d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
	}
}
int main() {
	int a = 0;
	int b = 0;
	int c = 0;
	while (true) {
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1) break;
		cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << "\n";
	}
}