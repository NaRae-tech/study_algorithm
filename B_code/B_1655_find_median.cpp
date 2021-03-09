#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	ios_base ::sync_with_stdio(false);
	cin.tie(0);

	int N = 0;
	cin >> N;

	priority_queue<int, vector<int>, less<int>> small;
	priority_queue<int, vector<int>,  greater<int>> big;
	int a = 0;

	while (N--) {
		cin >> a;
		
		if (small.size()>big.size()) {
			big.push(a);
		}
		else {
			small.push(a);
		}
		
		while (!small.empty() && !big.empty() &&!(small.top() <= big.top())) {
			int temp = small.top();
			small.pop();
			int temp2 = big.top();
			big.pop();
			small.push(temp2);
			big.push(temp);	
		}
		cout << small.top() << "\n";
	}
	return 0;
}