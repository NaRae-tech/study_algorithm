#include <iostream>
#include <string>
using namespace std;

int main() {
	string str = "";
	cin >> str;
	int checkingL[26] = { };
	for (int i = 0; i < 26; i++) {
		checkingL[i] = -1;
	}
	for (int i = 0; i < str.length(); i++) {
		int index = str[i] - 'a';
		if (checkingL[index] == -1) {
			checkingL[index] = i;
		}
	}
	for (int i = 0; i < 26; i++) {
		cout << checkingL[i] << ' ';
	}
	return 0;
}