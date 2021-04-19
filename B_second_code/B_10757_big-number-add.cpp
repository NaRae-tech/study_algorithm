#include <iostream>
#include <string>
using namespace std;

int main() {
	string A = "";
	string B = "";
	cin >> A >> B;

	int result[10001] = { 0, };
	int length = (A.size() > B.size()) ? B.size() : A.size();
	int index = 0;

	int up = 0;
	for (int i = 1; i <= length; i++) {
		int a = A[A.size() - i] - '0';
		int b = B[B.size() - i] - '0';
		result[index++] = (up + a + b) % 10;
		up = (up + a + b) / 10;
	}
	
	if (A.size() > B.size()) {
		for (int i = length + 1; i <= A.size(); i++) {
			int a = A[A.size() - i] - '0';
			result[index++] = (up + a) % 10;
			up = (up + a) / 10;
		}
		if (up != 0) result[index++] = up;
	}
	else if (B.size() > A.size()) {
		for (int i = length + 1; i <= B.size(); i++) {
			int b = B[B.size() - i] - '0';
			result[index++] = (up + b) % 10;
			up = (up + b) / 10;
		}
		if (up != 0) result[index++] = up;
	}
	else {
		if (up != 0) result[index++] = up;
	}

	for (int i = index - 1; i >= 0; i--) {
		cout << result[i];
	}
	return 0;
}