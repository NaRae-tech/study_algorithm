#include <iostream>
using namespace std;

unsigned long count(unsigned long a, unsigned long b) {
	unsigned long c = 0;
	while (a) {
		c += a / b;
		a /= b;
	}
	return c;
}
int main() {

	unsigned long N = 0;
	unsigned long M = 0;
	cin >> N >> M;

	unsigned long count_2 = 0;
	count_2 = count(N, 2) - count(N - M, 2) - count(M, 2);
	unsigned long count_5 = 0;
	count_5 = count(N, 5) - count(N - M, 5) - count(M, 5);
	cout << ((count_2 >= count_5) ? count_5 : count_2);

	return 0;
}