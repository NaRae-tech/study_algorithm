#include<iostream>
#include <vector>
using namespace std;

int main() {

	int N = 0;
	int M = 0;
	cin >> N >> M;
	vector<int>before(N + 1,1);
	vector<int>after(N + 1,1);
	
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0 || i == j) {
				after[j] = 1;
			}
			else {
				after[j] = before[j] + before[j - 1];
			}
		}
		before = after;
	}

	int temp = after[M];
	int count_2 = 0;
	int count_5 = 0;
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
	cout << ((count_2 >= count_5) ? count_5 : count_2);
	return 0;
}