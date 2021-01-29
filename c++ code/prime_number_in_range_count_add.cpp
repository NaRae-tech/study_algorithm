#include <iostream>
#include <vector>
using namespace std;

int main() {
	int range1 = 0;
	cin >> range1;
	int range2 = 0;
	cin >> range2;

	vector<int> primeNumber;
	for (int i = range1; i <= range2; i++) {
		bool flag = true;
		if (i == 1) flag = false;
		else if (i > 1) {
			for (int j = 2; j < i; j++) {
				if (i%j == 0) {
					flag = false;
					break;
				}
			}
		}
		if (flag == true) primeNumber.push_back(i);
	}


	if (primeNumber.size() == 0) {
		cout << -1 << endl;
	}
	else {
		int sum = 0;
		for (int i = 0; i < primeNumber.size(); i++) {
			sum += primeNumber[i];
		}
		cout << sum << "\n" << primeNumber[0] << endl;
	}


	return 0;
}