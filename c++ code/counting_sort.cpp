#include <iostream>

int main() {
	int T = 0;
	scanf("%d", &T);
	
	int number[10001] = { 0 };
	int max = 0;
	for (int i = 0; i < T; i++) {
		int n = 0;
		scanf("%d", &n);
		number[n]++;
		if (max < n) max = n;
	}
	for (int i = 1; i < max+1; i++) {
		if (number[i] > 0) {
			for (int j = 0; j < number[i]; j++) {
				printf("%d\n", i);
			}
		}
	}

	return 0;
}