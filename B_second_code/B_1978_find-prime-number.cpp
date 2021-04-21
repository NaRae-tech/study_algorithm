#include <iostream>
using namespace std;

int main() {

	int number[101] = { 0, };

	int N = 0;
	cin >> N;

	for (int i = 0; i < N; i++) { cin >> number[i]; }

	bool not_prime_number[101] = { false, };
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (number[i] == 1) {
			not_prime_number[i] = true;
		}
		for (int j = number[i] - 1; j > 1; j--) {
			if (number[i] % j == 0) {
				not_prime_number[i] = true;
			}
		}
		if (not_prime_number[i] == false) ++cnt;
	}
	cout << cnt;
	return 0;
}