#include <iostream>
#include <algorithm>
using namespace std;

int queen[15] = { -1, };
int cnt = 0;

bool checking(int index) {
	if (index == 0) return true;
	else {
		for (int i = 0; i < index; i++) {
			//같은 라인일때
			if (queen[i] == queen[index]) return false;
			//대각선 상에 존재할 때
			else if (abs(queen[index] - queen[i]) == index - i) return false;
		}
	}
	return true;
}

void chess(int index, int N) {
	if (index == N) { ++cnt; }
	else {
		for (int i = 0; i < N; i++) {
			//i값을 채용
			queen[index] = i;
			//i값이 조건에 만족했다면 다음 level로 진출
			if (checking(index)) chess(index + 1, N);
			//i값 채용 취소
			queen[index] = -1;
		}
	}
}

int main() {
	int N = 0;
	cin >> N;

	chess(0, N);
	cout << cnt;
	return 0;
}