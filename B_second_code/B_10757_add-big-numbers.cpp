#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	string A = "";
	string B = "";
	cin >> A;
	cin >> B;

	vector<int> iA;
	int index = A.size()-3;
	for (int i = 0; i < A.size() / 3; i++) {
		string temp = A.substr(index, 3);
		index -= 3;
		iA.push_back(stoi(temp));
	}
	if (A.size() % 3 == 1) { 
		string temp = A.substr(0, 1);
		iA.push_back(stoi(temp));
	}
	else if (A.size() % 3 == 2) { 
		string temp = A.substr(0,2);
		iA.push_back(stoi(temp));
	}

	vector<int> iB;
	index = B.size() - 3;
	for (int i = 0; i < B.size() / 3; i++) {
		string temp = B.substr(index, 3);
		index -= 3;
		iB.push_back(stoi(temp));
	}
	if (B.size() % 3 == 1) {
		string temp = B.substr(0, 1);
		iB.push_back(stoi(temp));
	}
	else if (B.size() % 3 == 2) {
		string temp = B.substr(0, 2);
		iB.push_back(stoi(temp));
	}

	int length = (iA.size() > iB.size()) ? iB.size() : iA.size();
	vector<string> result;
	int up = 0;
	for (int i = 0; i < length; i++) {
		result.push_back(to_string((up + iA[i] + iB[i])%1000));
		up = (up + iA[i] + iB[i]) / 1000;
	}
	if (iA.size() > iB.size()) {
		for (int i = length; i < iA.size(); i++) {
			result.push_back(to_string((iA[i]+up)%1000));
			up = (up+ iA[i] + up) / 1000;
		}
		if (up != 0) result.push_back(to_string(up));
	}
	
	else if (iB.size() > iA.size()) {
		for (int i = length; i < iB.size(); i++) {
			result.push_back(to_string((iB[i]+up)%1000));
			up = (up+iB[i] + up) / 1000;
		}
		if (up != 0) result.push_back(to_string(up));
	}
	else {
		if (up != 0) result.push_back(to_string(up));
	}
	for (int i = result.size()-1; i >=0 ; i--) {
		if (i != result.size() - 1 && result[i].size() == 1) cout << "00" << result[i];
		else if (i != result.size() - 1 && result[i].size() == 2) cout << "0" << result[i];
		else cout << result[i];
	}
	return 0;
}