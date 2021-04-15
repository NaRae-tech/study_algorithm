#include <iostream>
#include <string>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	while (T--) {
		int H = 0;
		int W = 0;
		int N = 0;
		cin >> H >> W >> N;

		int floor = N % H;
		if (floor == 0) { floor = H; }
		int room = N / H + 1;
		if (N%H == 0) { room -= 1; }
		string s = to_string(room);
		if (s.size() == 1) { s = "0" + s; }
		
		cout << floor << s << "\n";
	}

	return 0;
}