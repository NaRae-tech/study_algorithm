#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	cin >> N;

	int stair[302] = { 0, };
	int A = 0;
	for (int i = 0; i < N; i++) {
		cin >> A;
		stair[i] = A;
	}

	int dq[302] = { 0, };
	dq[0] = stair[0];
	dq[1] = max(stair[1], stair[0] + stair[1]);
	dq[2] = max(stair[0] + stair[2], stair[1] + stair[2]);
	for (int i = 3; i < N; i++) {
		//두 칸 전까지 합중에 제일 큰값 + 지금 계단 값
		//세칸 전까지 합 중에 제일 큰값 + 직전 계단 값 + 지금 계단값
		//둘 중 더 큰 족 채택
		dq[i] = max(dq[i - 2] + stair[i], dq[i - 3] + stair[i - 1] + stair[i]);
	}
	cout << dq[N - 1];
	return 0;
}