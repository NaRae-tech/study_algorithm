#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	cin.sync_with_stdio(0);
	int N = 0;
	cin >> N;
	queue<int> q;
	int a = 0;
	while (N--) {
		string commend = "";
		cin >> commend;
		if (commend == "push") {
			cin >> a;
			q.push(a);
		}
		else if (commend == "pop") {
			if (q.empty()) { cout << "-1\n"; }
			else{
				cout << q.front() << "\n";
				q.pop();
			}
		}
		else if (commend == "size") { cout << q.size() << "\n"; }
		else if (commend == "empty") { cout << q.empty() << "\n"; }
		else if (commend == "front") {
			if (q.empty()) { cout << "-1\n"; }
			else {cout << q.front() << "\n";}
		}
		else if (commend == "back") {
			if (q.empty()) { cout << "-1\n"; }
			else { cout << q.back() << "\n"; }
		}
	}
	return 0;
}