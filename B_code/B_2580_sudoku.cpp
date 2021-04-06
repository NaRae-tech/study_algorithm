#include<iostream>
#include <vector>
using namespace std;

int sudoku[9][9] = { 0, };
vector<vector<int>> emptyS;
bool finish = false; 

bool check(int x, int y) {
	for (int i = 0; i < 9; i++) {
		if (sudoku[x][i] == sudoku[x][y] && i!=y) return false;
		if (sudoku[i][y] == sudoku[x][y] && i!=x)return false;
	}
	for (int i = 3*(x / 3); i < 3*(x / 3) + 3; i++) {
		for (int j = 3*(y / 3); j < 3*(y / 3) + 3; j++) {
			if (sudoku[i][j] == sudoku[x][y]) 
				if(i!=x && j!=y) return false;
		}
	}
	return true;
}

void DFS(int index) {
	if (index == emptyS.size()) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << sudoku[i][j] << " ";
			}
			cout << "\n";
		}
		finish = true;
		return;
	}
	int x = emptyS[index][0];
	int y = emptyS[index][1];
	for (int k = 1; k <= 9; k++) {
		sudoku[x][y] = k;
		if (check(x, y) == true) DFS(index + 1);
		if (finish==true) return;
	}
	sudoku[x][y] = 0;
	return;
}

int main() {

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> sudoku[i][j];
			if (sudoku[i][j] == 0) emptyS.push_back({ i,j });
		}
	}
	DFS(0);
	return 0;
}