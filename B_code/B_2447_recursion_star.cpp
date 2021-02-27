#include <iostream>
using namespace std;
void calculate(int x, int y, int size) {
	if ((x/(size/3)) % 3 == 1 && (y/(size/3)) % 3 == 1) {
		cout<< ' ';
	}
	else {
		if (size / 3 == 1) {
			cout<<'*';
		}
		else {
			calculate(x, y, size/3);
		}
	}
}
void star(int size) {
	for (int y = 0; y < size; y++) {
		for (int x = 0; x < size; x++) {
			calculate(x,y,size);
		}
		cout << "\n";
	}
}

int main() {
	int N = 0;
	cin >> N;

	star(N);
	return 0;
}