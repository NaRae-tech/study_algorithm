#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {
	ll T = 0;
	cin >> T;
	while (T--) {
		ll X = 0;
		ll Y = 0;
		cin >> X >> Y;
		
		ll d = 1;
		while (d*d < Y - X) {
			++d;
		}
		--d;

		ll rest = (Y - X) - (d*d);
		rest = ceil((double)rest / 2);

		cout << d * 2 - 1 + rest << "\n";
	}
	
	return 0;
}