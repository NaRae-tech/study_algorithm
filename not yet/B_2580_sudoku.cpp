#include<iostream>
using namespace std;

int sudoku[9][9];
int* deleteC(int candidate[],int x, int y) {
	//세로, 가로
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (sudoku[x][j] == candidate[i]) candidate[i] = 0;
			if (sudoku[j][y] == candidate[i]) candidate[i] = 0;
		}
	}
	//사각형 
	return candidate
}
void check(int x, int y) {
	int candidate[9] = { 1,2,3,4,5,6,7,8,9 };
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (sudoku[i][j] == 0 ) {
				deleteC(candidate, i, j);

			}
		}
	}
}
int main() {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			int n = 0;
			cin >> n;
			sudoku[i][j] = n;
		}
	}
	check(0,0);
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << sudoku[i][j] << " ";
		}
		cout << "\n";
	}
	
	return 0;
}