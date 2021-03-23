#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	int number[100001];
	int dq[100001];
	int a = 0;
	for (int i = 0; i < N; i++) {
		cin >> a;
		number[i] = a;
	}

	dq[0] = number[0];
	int temp = dq[0];
	for (int i = 1; i < N; i++) {
		dq[i] = max(number[i], number[i] + dq[i - 1]);
		temp = max(temp, dq[i]);
	}
	cout << temp;

}