#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int main() {
	string s = "";
	cin >> s;

	int answer = 0;
	stack<char> rest;
	while(!s.empty()){
		if (s[0] == s[1]) {
			s.erase(0, 2);
		}
		else if (s[0] != s[1] && rest.empty()) {
			rest.push(s[0]);
			s.erase(0, 1);
		}
		else if (s[0] != s[1] && !rest.empty()) {
			if (rest.top() == s[0]) {
				s.erase(0, 1);
				rest.pop();
			}
			else {
				rest.push(s[0]);
			}
		}
	}
	if (s.empty() && rest.empty()) { answer = 1; }

	cout << answer;
	return 0;
}