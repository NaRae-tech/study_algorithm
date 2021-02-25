#include <iostream>
#include <queue>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	while (T--) {
		int N = 0;
		int M = 0;
		cin >> N >> M;

		queue<pair<int,int>> q;
		priority_queue<int>pq;
		int input = 0;
		for (int i = 0; i < N; i++) {
			cin >> input;
			pq.push(input);
			q.push(pair<int,int>(input, i));
		}
		
		int count = 0;
		while (true) {
			if (q.front().first == pq.top()) {
				++count;
				if (q.front().second == M) {
					break;
				}
				q.pop();
				pq.pop();
			}
			 else {
				 pair<int, int> temp = q.front();
				 q.pop();
				 q.push(temp);
			 }
		}
		cout << count << "\n";
	}
	return 0;
}