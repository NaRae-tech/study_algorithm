#include <iostream>
#include <vector>
#include <stack>
using namespace std;

typedef unsigned long long ll;

int main() {

	int N = 0;
	
	while (true) {
		cin >> N;
		if (N == 0) break;

		vector<ll> box(N, 0);
		for (int i = 0; i < N; i++) { cin >> box[i]; }

		stack<ll> result;
		ll r = 0;
		for (int i = 0; i < N; i++) {
			while (!result.empty() && box[result.top()]>box[i]) {
				ll h = box[result.top()];
				ll w = i;
				result.pop();
				if (!result.empty()) {
					w = (i - result.top() - 1);
				}
				if (r < w*h) { r = w * h; }
			}
			result.push(i);
		}

		while (!result.empty()) {
			ll h = box[result.top()];
			ll w = N;
			result.pop();
			if (!result.empty()) {
				w = (N - result.top() - 1);
			}
			if (r < w*h) { r = w * h; }
		}

		cout << r << "\n";
	}
	return 0;
}