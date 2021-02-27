#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
	string A = "";
	string B = "";
	cin >> A;
	cin >> B;

	int reverseA = 0;
	int reverseB = 0;
	
	for (int i = 0; i < 3; i++) {
		reverseA += (A[i] - '0')*pow(10, i);
		reverseB += (B[i] - '0')*pow(10, i);
	}

	cout << ((reverseA > reverseB) ? reverseA : reverseB )<< endl;

	return 0;
}