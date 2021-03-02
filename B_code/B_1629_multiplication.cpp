#include<iostream>
using namespace std;

long long int divisionAlgo(long long int A, long long int B, long long int C) {
	if (B == 0) {
		return 1;
	}
	else if (B == 1) {
		return A%C;
	}
	long long int temp = divisionAlgo(A, (int)(B/2), C);

	if (B % 2 == 0) {return (temp*temp) % C;}
	else { return (A*((temp*temp)%C)) % C; }

}
int main() {
	long long int A = 0;
	long long int B = 0;
	long long int C = 0;
	cin >> A >> B >> C;
	cout << divisionAlgo(A, B, C) << "\n";

	return 0;
}