#include <iostream>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	int changeList[4] = { 500,100,50,10 };
	int count = 0;
	for (int i = 0; i < 4; i++) {
		count += (N / changeList[i]);
		N %= changeList[i];
	}
	cout << count;
}