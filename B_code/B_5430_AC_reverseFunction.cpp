#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0);
	cin.sync_with_stdio(0);

	int T = 0;
	cin >> T;
	while (T--) {
		string commend = "";
		cin >> commend;
		int N = 0;
		cin >> N;
		
		string number = "";
		cin >> number;
		deque<int> dq;
		for (int i = 0; i < N; i++) {
			dq.push_back(static_cast<int>(number[2 * i + 1]-'0'));
		}

		bool flag = true;
		for (unsigned int i = 0; i < commend.size(); i++) {
			if (commend[i] == 'R') {
				reverse(dq.begin(), dq.end());
			}
			else if (commend[i] == 'D') {
				if (dq.empty()) {
					cout << "error" << "\n";
					flag = false;
					break;
				}
				dq.pop_front();
				--N;
			}
		}

		if (flag) {
			cout << "[";
			for (int i = 0; i < N - 1; i++) {
				cout << dq.front() << ",";
				dq.pop_front();
			}
			cout << dq.front() << "]\n";
		}
	}
	return 0;
}