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
		list.push_back(n);
		for (int i = 0; i < list.size(); i++) {
			for (int j = i; j < list.size(); j++) {
				if (list[j] < list[i]) {
					int temp = list[j];
					list[j] = list[i];
					list[i] = temp;
				}
			}
		}
	}

	for (int i = 0; i < list.size(); i++) {
		cout << list[i] << "\n";
	}
	return 0;
}