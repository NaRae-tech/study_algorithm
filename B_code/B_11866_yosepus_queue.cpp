#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int N = 0;
	int K = 0;
	cin >> N >> K;

	vector<int> member(N);
	for (int i = 1; i <= N; i++) { member[i - 1] = i; }
	queue <int> result;
	
	int index = K - 1;
	for (int i = 0; i < N; i++) {
		result.push(member[index]);
		member.erase(member.begin() + index);
		if (member.size() >1) {
			index = (index + K - 1 >= member.size()) ? (index + K - 1) % member.size() : (index + K - 1);
		}
		else {
			index = 0;
		}
	}

	cout << "<";
	while(result.size()>1){
		cout << result.front() << ", ";
		result.pop();
	}
	cout << result.front() << ">";
	return 0;
}