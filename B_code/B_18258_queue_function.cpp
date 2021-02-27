#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Q {
public:
	vector<int> v;
	void push(int x) { v.push_back(x); }
	void pop() {
		if (v.size() == 0) { cout << "-1\n"; }
		else {
			cout << v.front() << "\n";
			vector<int>::iterator iter = v.begin();
			v.erase(iter);
		}
	}
	void size() {cout << v.size() << "\n";}
	void empty() {
		if (v.size() == 0) { cout << "1\n"; }
		else { cout << "0\n"; }
	}
	void front() { 
		if (v.size() == 0) { cout << "-1\n"; }
		else { cout << v[0] << "\n"; }
	}
	void back(){
		if (v.size() == 0) { cout << "-1\n"; }
		else { cout << v[v.size()-1] << "\n"; }
	}
};

int main() {
	int N = 0;
	cin >> N;
	Q q;
	while (N--) {
		string commend = "";
		cin >> commend;
		if (commend == "push") {
			int a = 0;
			cin >> a;
			q.push(a);
		}
		else if (commend == "pop") { q.pop(); }
		else if (commend == "size") { q.size(); }
		else if (commend == "empty") { q.empty(); }
		else if (commend == "front") { q.front(); }
		else if (commend == "back") { q.back(); }
	}
	return 0;
}