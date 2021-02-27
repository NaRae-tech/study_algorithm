#include <iostream>
#include <vector>
using namespace std;

int main() {
	int range1 = 0;
	cin >> range1;
	int range2 = 0;
	cin >> range2;

	vector<bool> prime;
	prime.push_back(false);
	prime.push_back(false);
	for (int i = 2; i <= range2; i++) {
		prime.push_back(true);
	}

	for (int i = 2; i*i <= range2; i++) {
		if (prime[i] == true) {
			for (int j = i * i; j <= range2; j += i) {
				prime[j] = false;
			}
		}
	}
	
	for (int i = range1; i <= range2; i++) {
		if (prime[i] == true) {
			cout << i << "\n";
		}
	}

	return 0;
}