#include <iostream>
using namespace std;

int main() {
	int x = 0;
	cin >> x;
	int y = 0;
	cin >> y;
	int w = 0;
	cin >> w;
	int h = 0;
	cin >> h;

	int r1 = x - 0;
	int r2 = y - 0;
	int r3 = w - x;
	int r4 = h - y;

	int min1 = ((r1 >= r2) ? r2 : r1);
	int min2 = ((r3 >= r4) ? r4 : r3);

	cout << ((min1 >= min2) ? min2 : min1) << "\n";
}