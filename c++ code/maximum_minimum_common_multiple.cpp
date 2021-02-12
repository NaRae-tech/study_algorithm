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
/*int main() {
	int A = 0;
	int B = 0;
	cin >> A >> B;

	int maximum = 1;
	long minimum = 1;

	for (int i = 2; (i <= A) && (i <= B); i++) {
		if ((A%i == 0) && (B%i == 0)) {
			maximum *= i;
			A /= i;
			B /= i;
		}
	}
	minimum = A * B * maximum;
	cout << maximum << "\n" << minimum;
	return 0;
}*/