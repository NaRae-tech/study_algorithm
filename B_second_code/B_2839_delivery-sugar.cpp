#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;
	
	bool flag = false;
	for (int i = 0; i < N / 3+1; i++) {
		for (int j = 0; j < N / 5+1; j++) {
			if (3 * i + 5 * j == N) {
				cout << i + j;
				flag = true;
				break;
			}
		}
		if (flag == true) break;
	}
	if (flag == false) cout << -1;

	return 0;
}