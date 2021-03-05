#include <iostream>
using namespace std;

int column[16];
int cnt = 0;
bool check(int r) {
	//column배열에 이전것들과 다른 열인지
	//column 배열의 이전 것 들과 대각선은 아닌지
	//확인해서 결과값 return 
	bool flag = true;
	for (int i = 0; i < r; i++) {
		//1행~지금 확인하려는 행 바로 직전까지의 column의 값을
		//내가 column[r]에 넣은 값과 비교하여 조건확인
	}
	return flag;
}
void bfs(int row, int N) {
	// 행값을 파라미터로 받고
	// 열값은 for문을이용해서 안에서 계산
	if (check(row)) {
		if (row == N) {
			++cnt;
		}
		else {
			for (int i = 0; i < N; i++) {

			}
		}
	}
}
int main() {
	int N = 0;
	cin >> N;
	bfs(0,N);
	return 0;
}