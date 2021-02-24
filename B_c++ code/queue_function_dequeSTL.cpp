#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	deque<int>dq;
	int a = 0;
	string commend = "";

	while (N--) {
		cin.tie(0);
		cin.sync_with_stdio(0);
		cin >> commend;
		if (commend == "push") {
			cin >> a;
			dq.push_back(a);
		}
		else if (commend == "pop") {
			if (dq.empty()) { cout << "-1\n"; }
			else {
				cout << dq.front() << "\n";
				dq.pop_front();
			}
		}
		else if (commend == "size") { cout << dq.size() << "\n"; }
		else if (commend == "empty") { cout << dq.empty() << "\n"; }
		else if (commend == "front") {
			if (dq.empty()) { cout << "-1\n"; }
			else { cout << dq.front() << "\n"; }
		}
		else if (commend == "back") {
			if (dq.empty()) { cout << "-1\n"; }
			else { cout << dq.back() << "\n"; }
		}
	}
	return 0;
}