#include <iostream>
#include <vector>
using namespace std;

int main() {

	bool index[10001] = {true};
	for (int i = 0; i <= 10000; i++) {
		if (i == 0 || i == 1)index[i] = false;
		else index[i] = true;
	}
	for (int i = 2; i <= 10000; i++) {
		if (index[i]) {
			for (int j = 2 * i; j <= 10000; j += i) {
				index[j] = false;
			}
		}
	}

	int T = 0;
	cin >> T;

	while (T--) {
		int N = 0;
		cin >> N;

		vector <int> vA;
		vector <int> vB;
		vector <pair<int, int>> vAB;
		int A = 0;
		int B = 0;
		for (int i = 2; i < N; i++) {
			if (index[i]== true && index[N - i]==true) {
				vAB.push_back(make_pair(i, N - i));
			}
		}
		int min = N;
		for (unsigned int i = 0; i < vAB.size(); i++) {
			if (vAB[i].second - vAB[i].first >= 0 && vAB[i].second - vAB[i].first < min) {
				A = vAB[i].first;
				B = vAB[i].second;
			}
		}
		cout << A << " " << B << "\n";
	}
	return 0;
}