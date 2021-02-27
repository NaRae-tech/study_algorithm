#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	vector <int> v;
	for (int i = 1; i <= N; i++) {
		v.push_back(i);
	}

	while (v.size() > 1) {
		v.erase(v.begin());
		if (v.size() == 1) { break; }
		else {
			v.push_back(v[0]);
			v.erase(v.begin());
		}
	}
	
	cout << v.front() << "\n";
	return 0;
}