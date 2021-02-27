#include <iostream>
#include <string>
using namespace std;

int main() {
	int N = 0;
	cin >> N;
		
	int count_2 = 0;
	int count_5 = 0;

	for (int i = 1; i <= N; i++) {
		int temp = i;
		bool flag = false;
		while (true) {
			if ((temp % 2 == 0) || (temp % 5 == 0)) {
				if (temp % 2 == 0) {
					++count_2;
					temp /= 2;
				}
				else if (temp % 5 == 0) {
					++count_5;
					temp /= 5;
				}
			}
			else break;
		}
	}
	cout << ((count_2 >= count_5) ? count_5 : count_2) << "\n";
	return 0;
}