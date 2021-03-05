#include <iostream>
#include <vector>
using namespace std;
void calculate(int numberList[12], int operate[4], vector<int>result) {

}
int main() {
	int T = 0;
	cin >> T;
	
	int numberList[12] = { 0 };
	for (int i = 0; i < T; i++) {
		cin >> numberList[i];
	}

	int operate[4] = { 0 };
	for (int i = 0; i < 4; i++) {
		cin >> operate[i];
	}

	vector<int>result;
	calculate(numberList, operate, result);
	int max = result[0];
	int mini = result[0];
	for (unsigned int i = 0; i < result.size(); i++) {
		if (result[i] > max) max = result[i];
		if (result[i] < mini) mini = result[i];
	}
	cout << max << "\n" << mini;

	return 0;
}