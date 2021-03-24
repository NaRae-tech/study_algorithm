#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;
	
	int wine[10001] = { 0, };
	int a = 0;
	for (int i = 3; i < N+3; i++) {
		cin >> a;
		wine[i] = a;
	}
	
	int maximum = 0;
	int dq[10001] = { 0, };
	for (int i = 3; i < N+3; i++) {
		dq[i] = max(dq[i - 3] + wine[i - 1] + wine[i], dq[i - 2] + wine[i]);
		dq[i] = max(dq[i - 1], dq[i]);
		maximum = max(dq[i], maximum);
	}

	cout << maximum;
	return 0;
}