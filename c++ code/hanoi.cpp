#include <iostream>
#include <cmath>
using namespace std;

void move(int from, int to) {
	cout << from << " " << to << "\n";
}
void hanoi(int now, int start, int via, int finish) {
	if (now == 1) {
		move(start, finish);
		return;
	}
	else {
		hanoi(now - 1, start, finish, via);	// 이동해야하는 n원반위 n-1개의 원반을 경유지로 이동
		move(start, finish);				// n 원반을 종착지로 이동
		hanoi(now - 1, via, start, finish);	// via에 있는 n-1개의 원반을 종착지로 이동
	}
}
int main() {
	int N = 0;
	cin >> N;

	
	cout << (long long int) pow(2, N) - 1 << "\n";
	hanoi(N, 1, 2, 3);
}
/*#include <iostream>
#include <vector>
using namespace std;


vector<pair<int, int>> list;
void move(char from, char to) {
	int start = 0;
	int finish = 0;

	if (from == 'A') start = 1;
	else if (from == 'B') start = 2;
	else if (from == 'C') start = 3;
	if (to == 'A') finish = 1;
	else if (to == 'B') finish = 2;
	else if (to == 'C') finish = 3;
	
	list.push_back(make_pair(start, finish));
}
void hanoi(int now, char start, char via, char finish) {
	if (now == 1) {
		move(start, finish);
		return;
	}
	else {
		hanoi(now - 1, start, finish, via);	// 이동해야하는 n원반위 n-1개의 원반을 경유지로 이동
		move(start, finish);					// n 원반을 종착지로 이동
		hanoi(now - 1, via, start, finish);	// via에 있는 n-1개의 원반을 종착지로 이동
	}
}
int main() {
	int N = 0;
	cin >> N;
	
	hanoi(N, 'A', 'B', 'C');

	cout << list.size() << "\n";
	for (unsigned int i = 0; i < list.size(); i++) {
		cout << list[i].first << " " << list[i].second << "\n";
	}
}*/