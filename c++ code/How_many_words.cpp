#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	string S = " ";
	getline(cin, S);

	istringstream SS(S);
	string tempS = " ";
	
	int count = 0;
	while (getline(SS, tempS, ' ')) {
		if (tempS != "") {
			count++;
		}
	}
	cout << count << endl;
	return 0;
}