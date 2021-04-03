#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long ll;
typedef vector<vector<ll>> matrix;

matrix operator*(matrix &f, matrix &s) {
	matrix calculate(2, vector < ll>(2));
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			ll answer = 0;
			for (int a = 0; a < 2; a++) {
				answer += (f[i][a] * s[a][j]) % 1000000007;
			}
			calculate[i][j] = answer % 1000000007;
		}
	}
	return calculate;
}
matrix power(matrix now, ll N){
	matrix unit(2, vector<ll>(2));
	unit = { {1,1},{1,0} };

	while (N > 0) {
		if (N % 2 == 1) {
			now = unit * now;
		}
		N /= 2;
		unit = unit * unit;
	}
	return now;
}

int main() {
	ll N = 0;
	cin >> N;

	if (N <= 1) cout << N << "\n";
	else {
		matrix now(2, vector<ll>(2));
		now = { {1,0},{0,1} };

		matrix result = power(now, N);
		cout << result[0][1] << "\n";
	}
	return 0;
}