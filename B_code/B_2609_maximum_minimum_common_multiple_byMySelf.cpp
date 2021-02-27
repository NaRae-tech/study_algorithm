#include <iostream>
using namespace std;
int main() {
	int A = 0;
	int B = 0;
	cin >> A >> B;

	int maximum = 1;
	long minimum = 1;

	int i = 2;
	while ((i <= A) && (i <= B)) {
		if ((A%i == 0) && (B%i == 0)) {
			maximum *= i;
			A /= i;
			B /= i;
		}
		else {
			++i;
		}
	}
	minimum = A * B * maximum;
	cout << maximum << "\n" << minimum;
	return 0;
}