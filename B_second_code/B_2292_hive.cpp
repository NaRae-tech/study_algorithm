#include <iostream>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	if (N == 1) cout << "1";
	else {
		int start = 2;
		int level = 1;
		int end = start + 6*level;
		while (true) {
			if (start <= N && N < end) { 
				cout << level + 1;
				break;
			}
			else {
				start = end;
				++level;
				end = start + 6 * level;
			}
		}
		
	}
	return 0;
}