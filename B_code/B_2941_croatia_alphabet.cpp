#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
	string S = "";
	getline(cin, S);

	int numS = 0;

	for (int i = 0; i < S.length(); i++) {
		if (S[i] == 'c') {
			if (S[i + 1] == '-' || S[i + 1] == '=') {
				i += 1;
				numS++;
			}
			else numS++;
		}
		else if (S[i] == 'd') {
			if (S[i + 1] == '-' ) {
				i += 1;
				numS++;
			}
			else if (S[i + 1] == 'z' &&S[i + 2] == '=') {
				i += 2;
				numS++;
			}
			else numS++;
		}
		else if ((S[i] == 'l'&&S[i + 1] == 'j') || (S[i] == 'n'&&S[i + 1] == 'j')) {
			i += 1;
			numS++;
		}
		else if ((S[i] == 's'&&S[i + 1] == '=') || (S[i] == 'z'&&S[i + 1] == '=')) {
			i += 1;
			numS++;
		}
		else numS++;
	}
	cout << numS << endl;
	return 0;
}