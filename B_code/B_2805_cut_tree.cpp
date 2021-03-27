#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

long long cutTree(vector<long long > t, int N, int h) {
	long long  total = 0;
	for (int i = 0; i < N; i++) {
		if (t[i] - h >= 0) total += (t[i] - h);
	}
	return total;
}
int main() {
	int N = 0;
	int M = 0;
	cin >> N >> M;

	vector<long long >tree(N);
	int maximum = 0;
	for (int i = 0; i < N; i++) {
		cin >> tree[i];
		if (maximum < tree[i]) { maximum = tree[i]; }
	}

	int left = 0;
	int right = maximum;
	long long  middle = 0;
	long long  length = 0;
	long long  result = 0;
	while (left <= right) {
		middle = ceil((left + right) / 2);
		length = cutTree(tree, N, middle);
		if (length >= M) { 
			result = middle;
			left = middle+1; 
		}
		else { right = middle-1; }
	}

	cout << result;

	return 0;
}