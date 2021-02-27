#include <iostream>
#include <string>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	while (T--) {
		int N = 0;
		cin >> N;
		string S = " ";
		cin >> S;
		string newS = "";
		for (int i = 0; i < S.length(); i++) {
			for (int j = 0; j < N; j++) {
				newS += S[i];
			}
		}
		cout << newS << endl;
	}
	return 0;
}