#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
int gcd(int a, int b) {
	while (b != 0) {
		int n = a % b;
		a = b;
		b = n;
	}
	return a;
}
int main() {
	int N = 0;
	cin >> N;
	vector<int> numbers;
	for (int i = 0; i < N; i++) {
		int n = 0;
		cin >> n;
		numbers.push_back(n);
	}
	sort(numbers.begin(), numbers.end());
	if (numbers.size() == 1) {
		cout << numbers[0] * numbers[0];
	}
	else {
		int gcd_n = (numbers[0] * numbers[1]) / gcd(numbers[0], numbers[1]);
		for (int i = 2; i < N; i++) {
			gcd_n = (gcd_n*numbers[i]) / gcd(gcd_n, numbers[i]);
		}
		cout << ((gcd_n == numbers[int(numbers.size() - 1)]) ? gcd_n * numbers[0] : gcd_n);
	}
	return 0;
}