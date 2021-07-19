#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	vector<int>progresses = { 93,30,55 };
	vector<int>speeds = { 1,30,5 };

	vector<int> answer;
	
	vector<double> cal;
	for (unsigned int i = 0; i < progresses.size(); i++){
		cal.push_back(ceil((double)(100 - progresses[i]) / (double)speeds[i]));
	}
	
	double standard = cal[0];
	int count = 1;
	for (unsigned int i = 1; i < cal.size(); i++) {
		if (standard < cal[i]) {
			answer.push_back(count);
			standard = cal[i];
			count = 1;
		}
		else {
			count++;
		}
	}
	answer.push_back(count);

	for (unsigned int i = 0; i < answer.size(); i++) {
		cout << answer[i] << " ";
	}
	return 0;
}