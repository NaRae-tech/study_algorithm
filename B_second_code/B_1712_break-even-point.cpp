#include <iostream>
#include <cmath>
using namespace std;


int main() {
	int fixed = 0;
	int variable = 0;
	int cost = 0;
	cin >> fixed >> variable >> cost;

	//손익 분기점이 존재하지 않음
	if (variable >= cost) cout << "-1";
	else {
		//지출의 합 == 수익 => 다음 해부터 이익 발생
		//지출의 합 < 수익 => 그 해부터 이익 발생
		//둘다 소수점 버림 +1 
		cout << fixed / (cost - variable) + 1;
	}
	return 0;
}