#include <iostream>
using namespace std;

int gcd(int a, int b) {
	int n = 1;
	while (b != 0) {
		n = a % b;
		a = b;
		b = n;
	}
	return a;
}
int main() {
	int A = 0;
	int B = 0;
	cin >> A >> B;
	cout << gcd(A, B) << "\n" << (A*B) / gcd(A, B);

}