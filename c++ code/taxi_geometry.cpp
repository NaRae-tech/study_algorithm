#include <iostream>
using namespace std;

int main() {

	double R = 0;
	cin >> R;

	cout << fixed;
	cout.precision(6);
	double pi = 3.14159265358979;		
	cout << R * R*pi << endl;
	cout << R * R * 2 << endl;

	return 0;
}