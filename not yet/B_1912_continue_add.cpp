#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int N = 0;
	cin >> N;

	vector<int> number;
	int a = 0;
	int maximum = -1000;
	for (int i = 0; i < N; i++) {
		cin >> a;
		if (a > maximum) { maximum = a; }
		number.push_back(a);
	}

	vector<int> addNum;
	int sum = 0;
	int sumMax = 0;
	for (int i = 0; i < N; i++) {
		if (number[i] >= 0) {
			sum += number[i];
		}
		else {
			if (sum != 0) {
				addNum.push_back(sum);
				sum = 0;
			}
			addNum.push_back(number[i]);
		}
	}
	
	
	return 0;
}