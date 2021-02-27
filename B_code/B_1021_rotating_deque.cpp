#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main() {
	int N = 0;
	int M = 0;
	cin >> N >> M;

	vector<int>number(M);
	int a = 0;
	for (int i = 0; i < M; i++) {
		cin >> a;
		number[i] = a;
	}

	deque<int>dq;
	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}

	int count = 0;
	while (number.size() != 0) {
		//1번 연산
		if (number.front() == dq.front()) {
			number.erase(number.begin());
			dq.pop_front();
		}
		else {
			//2번연산이 좋을지 3번 연산이 좋을지 판단
			//내가 찾아야하는 숫자 기준 
			// 오른쪽에 수가 더 많으면 2번
			// 왼쪽에 수가 더 많으면 3번
			int index = 0;
			for (int k = 0; k < dq.size(); k++) {
				if (dq[k] == number.front()) {
					index = k;
				}
			}
			//2번연산
			if ((dq.size() - index) > (dq.size() / 2)) {
				++count;
				dq.push_back(dq.front());
				dq.pop_front();
			}
			//3번 연산
			else {
				++count;
				dq.push_front(dq.back());
				dq.pop_back();
			}
		}
	}
	cout << count << "\n";
	return 0;
}