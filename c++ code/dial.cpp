#include <iostream>
#include <string>
using namespace std;

int main() {
	string S = "";
	cin >> S;

	int count = 0;
	for (int i = 0; i < S.length(); i++) {
		if (S[i] == 'A' || S[i] == 'B' || S[i] == 'C') count += 3;
		else if (S[i] == 'D' || S[i] == 'E' || S[i] == 'F') count += 4;
		else if (S[i] == 'G' || S[i] == 'H' || S[i] == 'I') count += 5;
		else if (S[i] == 'J' || S[i] == 'K' || S[i] == 'L') count += 6;
		else if (S[i] == 'M' || S[i] == 'N' || S[i] == 'O') count += 7;
		else if (S[i] == 'P' || S[i] == 'Q' || S[i] == 'R' || S[i] == 'S') count += 8;
		else if (S[i] == 'T' || S[i] == 'U' || S[i] == 'V') count += 9;
		else if (S[i] == 'W' || S[i] == 'X' || S[i] == 'Y' || S[i] == 'Z') count += 10;
		else count += 11;
	}
	cout << count << endl;

	return 0;
}