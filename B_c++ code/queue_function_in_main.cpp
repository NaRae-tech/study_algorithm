#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	cin.tie(0); 
	cin.sync_with_stdio(0);
	int N = 0;
	cin >> N;

	vector<int>v;
	while (N--) {
		string commend = "";
		cin >> commend;
		if (commend == "push") {
			int a = 0;
			cin >> a;
			v.push_back(a);
		}
		else if (commend == "pop") {
			if (v.size() == 0) { cout << "-1\n"; }
			else {
				cout << v[0] << "\n";
				v.erase(v.begin());
			}
		}
		else if (commend == "size") { cout << v.size() << "\n"; }
		else if (commend == "empty") {cout << v.empty() << "\n";}
		else if(commend == "front"){
			if (v.size() == 0) { cout << "-1\n"; }
			else { cout << v.front() << "\n"; }
		}
		else if (commend == "back") {
			if (v.size() == 0) { cout << "-1\n"; }
			else { cout << v.back() << "\n"; }
		}
	}
	return 0;
}