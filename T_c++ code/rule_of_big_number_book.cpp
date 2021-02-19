#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N = 0;
	int M = 0;
	int K = 0;
	cin >> N >> M >> K;

	vector<int> numbers;
	for (int i = 0; i < N; i++) {
		int a = 0;
		cin >> a;
		numbers.push_back(a);
	}
	sort(numbers.begin(), numbers.begin() + N, greater<int>());

	//최대 숫자가 K개, 그 다음 큰수가 1번 더해진 횟수 K+1
	//M이 K+1로 나눠질 경우
	int count = int(M / (K + 1))*K;
	//M이 K+1로 나눠지지 않을 경우
	count += M % (K + 1);

	int result = 0;
	result += count * numbers[0];
	result += (M - count)*numbers[1];

	cout << result;
	return 0;
}