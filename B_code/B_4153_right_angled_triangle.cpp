#include <iostream>
using namespace std;

int main() {
	while (true) {
		unsigned long long int A = 0;
		unsigned long long int B = 0;
		unsigned long long int C = 0;
		cin >> A;
		cin >> B;
		cin >> C;
		if (A == 0 && B == 0 && C == 0)break;

		bool flag = false;
		if (A*A + B * B == C * C) flag = true;
		else if (A*A + C * C == B * B) flag = true;
		else if (B*B + C * C == A * A) flag = true;

		if (flag) cout << "right\n";
		else cout << "wrong\n";
	}

	return 0;
}