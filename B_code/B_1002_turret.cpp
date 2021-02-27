#include <iostream>
#include <cmath>
using namespace std;

int main() {
	
	int T = 0;
	cin >> T;
	while (T--) {
		int point = 0;
		int x1, y1, r1, x2, y2, r2;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		double d = (pow((x2 - x1), 2) + pow((y2 - y1), 2));
		double add = pow(r1 + r2, 2);
		double minus = pow(r1 - r2, 2);

		if (d == 0) {
			if (r1 == r2) point = -1;
			else point = 0;
		}
		else {
			if (add == d || minus == d) point = 1;
			else if (minus < d &&d < add) point = 2;
			else point = 0;
		}

		cout << point << "\n";
	}
	return 0;
}