#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	
	int prime = 0;

	vector<int> index;
	for (int i = 0; i < T; i++) {
		int n = 0;
		cin >> n;
		index.push_back(n);
	}

	for (int i = 0; i < T; i++) {
		bool flag = true;
		if (index[i] == 1) {
			flag = false;
		}
		else if (index[i] > 1) {
			for (int j = 2; j < index[i]; j++) {
				if (index[i] % j == 0) {
					flag = false;
				}
				if (flag == false) { break; }
			}
		}
		if (flag == true) prime++;
	}

	cout << prime << endl;

	return 0;
}