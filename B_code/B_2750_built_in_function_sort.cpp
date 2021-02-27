#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	vector<int> list;

	while (T--) {
		int n = 0;
		cin >> n;
		list.push_back(n);
	}
	sort(list.begin(),list.end());

	for (unsigned int i = 0; i < list.size(); i++) {
		cout << list[i] << "\n";
	}
	return 0;
}