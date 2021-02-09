#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	cin >> T;

	int* list = new int(T+1);
	//0번째에는 미포함을 위해 쓰레기값 포함
	list[0] = 1000001;
	for (int a = 1; a < T + 1; a++) {
		int n = 0;
		cin >> n;
		list[a] = n;
		for (int i = a; i > 0; i /= 2) {
			if (list[i] > list[i / 2]) {
				int temp = list[i / 2];
				list[i / 2] = list[i];
				list[i] = temp;
			}
			else {
				break;
			}
		}
	}

	int* sorted = new int(T + 1);
	for (int k = 0; k < T+1; k++) {
		sorted[k] = 0;
	}
	for (int i = T; i > 0; i--) {
		sorted[i] = list[1];
		list[1] = list[i];
		for (int k = i - 1; k > 1; k--) {
			for (int j = k; j > 0; j /= 2) {
				if (list[j] > list[j / 2]) {
					int temp = list[j / 2];
					list[j / 2] = list[j];
					list[j] = temp;
				}
				else {
					break;
				}
			}
		}
	}
	for (int i = 1; i < T + 1; i++) {
		cout << sorted[i] << "\n";
	}
	return 0;
}