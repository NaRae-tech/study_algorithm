#include <iostream>
#include <string>
using namespace std;
int main() {
	string str = " ";
	cin >> str;
	int check[26] = { 0 };
	for (int i = 0; i < str.length(); i++) {
		check[toupper(str[i]) - 'A']++;
	}

	int max = check[0];
	int maxInd = 0;
	for (int i = 1; i < 26; i++) {
		if (max < check[i]) {
			max = check[i];
			maxInd = i;
		}
		else if (max == check[i]) {
			maxInd = -1;
		}
	}
	if (maxInd == -1) cout << "?" << endl;
	else cout << char('A' + maxInd) << endl;

	return 0;
}