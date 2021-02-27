#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	cin >> T;

	vector<int> list;

	while (T--) {
		int n = 0;
		cin >> n;
		if (list.size() == 0) list.push_back(n);
		else if (list.size() == 1) {
			if (list[0] > n) list.insert(list.begin(), n);
			else list.push_back(n);
		}
		else {
			for (unsigned int i = 0; i < list.size(); i++) {
				if (list[i] >= n) {
					list.insert(list.begin() + i, n);
					break;
				}
				else if (list[i] < n && i == list.size() - 1) {
					list.push_back(n);
					break;
				}
			}
		}
	}
	for (int i = 0; i < list.size(); i++) {
		cout << list[i] << "\n";
	}
	return 0;
}