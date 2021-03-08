#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void del(vector<long> &d) {
	d[1] = d[d.size() - 1];
	d.erase(d.end()-1);
	int now = 1;

	long mini = 0;
	int miniInd = 1;

	
	while (2*now<d.size()) {
		mini = d[2 * now];
		miniInd = 2 * now;
		if (2 * now + 1 < d.size()) {
			if (abs(d[2 * now]) == abs(d[2 * now + 1])) {
				if (d[2 * now] > d[2 * now + 1])  {
					mini = d[2 * now + 1];
					miniInd = 2 * now + 1;
				}
			}
			else if (abs(d[2 * now]) > abs(d[2 * now + 1])) {
				mini = d[2 * now + 1];
				miniInd = 2 * now + 1;
			}
		}
		if (abs(mini) < abs(d[now])) {
			long temp2 = d[now];
			d[now] = mini;
			d[miniInd] = temp2;
			now = miniInd;
		}
		else if (abs(mini) == abs(d[now])) {
			if (mini < d[now]) {
				long temp2 = d[now];
				d[now] = mini;
				d[miniInd] = temp2;
				now = miniInd;
			}
			else break;
		}
		else { break; }
	}
}

void in(vector<long> &list, long a) {
	list.push_back(a);
	int child = list.size() - 1;
	int parent = (int)(child / 2);
	while (child > 1) {
		if (abs(list[parent]) < abs(list[child])) break;
		else if (abs(list[parent]) == abs(list[child])
			&& list[parent] < list[child]) break;
		else {
			long temp = list[child];
			list[child] = list[parent];
			list[parent] = temp;
			child = parent;
			parent /= 2;
		}
	}
}
int main() {
	int T = 0;
	cin >> T;

	vector<long> list;
	list.push_back(0);
	long a = 0;
	while (T--) {
		cin >> a;
		if (a == 0) {
			if (list.size() == 1) {
				cout << "0\n";
			}
			else {
				cout << list[1] << "\n";
				del(list);
			}
		}
		else {
			in(list, a);
		}
	}
	return 0;
}