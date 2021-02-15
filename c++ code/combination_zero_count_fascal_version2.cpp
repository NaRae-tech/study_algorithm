#include <iostream>
#include <vector>
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

	vector<unsigned long> before(N + 1,1);
	vector<unsigned long> after(N + 1,1);
	for (unsigned long i = 0; i <= N; i++) {
		for (unsigned long j = 0; j <= i; j++) {
			if (i == j || j == 0) {
				after[j] = 1;
			}
			else {
				after[j] = before[j - 1] + before[j];
			}
		}
		before = after;
	}

	unsigned long count_2 = count(after[M], 2);
	unsigned long count_5 = count(after[M], 5);

	cout << (count_2 >= count_5 ? count_5 : count_2);
	return 0;
}