#include<iostream>
#include<queue>
#include <algorithm>
using namespace std;

int main() {
	int T = 0;
	cin >> T;

	int a = 0;
	priority_queue<int, vector<int>, greater<int>> positive;
	priority_queue<int, vector<int>, less<int>> negative;
	while (T--) {
		cin >> a;
		if (a == 0) {
			if (positive.empty() && negative.empty()) cout << "0\n";
			else {
				if (negative.empty()) {
					cout << positive.top() << "\n";
					positive.pop();
				}
				else if(positive.empty()) {
					cout << negative.top() << "\n";
					negative.pop();
				}
				else {
					if (abs(negative.top()) < abs(positive.top())) {
						cout << negative.top() << "\n";
						negative.pop();
					}
					else if (abs(negative.top()) == abs(positive.top())) {
						cout << negative.top() << "\n";
						negative.pop();
					}
					else if (abs(negative.top()) > abs(positive.top())) {
						cout << positive.top() << "\n";
						positive.pop();
					}
				}
			}
		}
		else {
			if (a > 0) positive.push(a);
			else  negative.push(a); 
		}
	}
	return 0;
}