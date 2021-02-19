#include <iostream>
using namespace std;
int main() {

	int pointX = 0;
	int pointY = 0;

	int pointL[3][2] = { 0,0,0,0,0,0 };
	for (int i = 0; i < 3; i++) {
		int x = 0;
		int y = 0;
		cin >> x;
		cin >> y;
		pointL[i][0] = x;
		pointL[i][1] = y;
	}

	bool xflag = false;
	bool yflag = false;
	int otherX = 0;
	int otherY = 0;

	for (int j = 1; j < 3; j++) {
		if (pointL[0][0] == pointL[j][0]) {
			xflag = true;
		}
		else {
			otherX = pointL[j][0];
		}
	}
	((xflag == true) ? pointX = otherX : pointX = pointL[0][0]);

	for (int j = 1; j < 3; j++) {
		if (pointL[0][1] == pointL[j][1]) {
			yflag = true;
		}
		else {
			otherY = pointL[j][1];
		}
	}
	((yflag == true) ? pointY = otherY : pointY = pointL[0][1]);

	cout << pointX << " " << pointY << "\n";

	return 0;
}