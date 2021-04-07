#include <iostream>
#include <vector>
using namespace std;

int number[12] = { 0, };
int operators[4] = { 0, };
int maximum = -1000000000;
int minimum = 1000000000;

void calculate(int N, int index, int result) {
	if (index == N) {
		if (result > maximum) maximum = result;
		if (result < minimum) minimum = result;
		return;
	}
	else {
		for (int i = 0; i < 4; i++) {
			if (operators[i] > 0) {
				operators[i]--; //i번째 기호를 채용
				if (i == 0) calculate(N, index + 1, result + number[index]);
				else if (i == 1) calculate(N, index + 1, result - number[index]);
				else if (i == 2) calculate(N, index + 1, result * number[index]);
				else calculate(N, index + 1, result / number[index]);
				operators[i]++; //i번째 기호를 채용한 경우를 취소
			}
		}
	}
}

int main() {
	int N = 0;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> number[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> operators[i];
	}

	calculate(N, 1, number[0]);

	cout << maximum << "\n" << minimum;
	return 0;
}