#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int N = 0;
	cin >> N;
	
	vector<int>sequence;
	int a = 0;
	for (int i = 0; i < N; i++) {
		cin >> a;
		sequence.push_back(a);
	}
	
	vector<int> dq(N, 1);
	int maximum = 1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < i; j++) {
			if (sequence[i] > sequence[j]) {
				dq[i] = max(dq[i], dq[j] + 1);
			}
		}
		maximum = ((dq[i] > maximum) ? dq[i] : maximum);
	}
	cout<<maximum<<"\n";
	return 0;
}