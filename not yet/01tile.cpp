#include <iostream>
using namespace std;
long double factorial(int a) {
	long double result = 1;
	while (a>0) {
		result *= (a--);
	}
	return result;
}
int main() {
	int N = 0;
	cin >> N;

	int max00tile = N / 2;
	long double result = 0;
	for (int i = 0; i <= max00tile; i++) {
		int zerotile = 2 * i;
		int onetile = N - zerotile;
		result += (factorial(onetile + i) / (factorial(onetile)*factorial(i)));
	}
	cout << fixed;
	cout.precision(0);
	cout << result << "\n";
	return 0;
}