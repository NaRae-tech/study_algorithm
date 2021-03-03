#include <iostream>
#include <vector>
using namespace std;

vector<long long int> dt = { 0,1,2 };
void tile(int n) {
	for (int i = 3; i <= n; i++) {
		dt.push_back((dt[i - 1] + dt[i - 2]) % 15746);
	}
}
int main() {
	int N = 0;
	cin >> N;
	tile(N);
	cout << dt[N]%15746 << "\n";
	return 0;
}