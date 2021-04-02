#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<long long>> matrix;
int N = 0;
long long B = 0;

matrix operator* (matrix &first, matrix &second) {
	matrix calculate(N, vector<long long>(N));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int answer = 0;
			for (int a = 0; a < N; a++) {
				answer += ((first[i][a] % 1000) * (second[a][j] % 1000) % 1000);
			}
			calculate[i][j] = answer % 1000;
		}
	}
	return calculate;
}

matrix power(matrix origin) {
	matrix unit(N, vector<long long>(N));
	for (int i = 0; i < N; i++) {
		unit[i][i] = 1;
	}

	while (B > 0) {
		if (B % 2 == 1) {
			unit = unit * origin;
		}
		B /= 2;
		origin = origin * origin;
	}
	return unit;
}

void print(matrix mat) {
	mat = power(mat);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << mat[i][j] << " ";
		}
		cout << "\n";
	}
}

int main() {
	cin >> N >> B;

	matrix origin(N, vector<long long>(N));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> origin[i][j];
		}
	}
	   
	print(origin);

	return 0;
}
