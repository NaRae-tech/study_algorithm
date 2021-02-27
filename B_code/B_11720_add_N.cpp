#include <iostream>
#include <string>
using namespace std;
int main() {
	int N = 0;
	cin >> N;
	string str = "";
	cin >> str;
	int sum = 0;
	for (int i = 0; i < N; i++) {
		sum += static_cast<int>(str[i]-'0');
	}
	cout << sum;
	return 0;
}