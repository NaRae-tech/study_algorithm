#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	cin >> T;

	vector<string> words;
	cin.ignore();

	for (int i = 0; i < T;i++) {
		string temp = " ";
		getline(cin, temp);
		for (int i = 0; i < temp.length(); i++) {
			temp[i] = tolower(temp[i]);
		}
		words.push_back(temp);
	}

	int checker = 0;
	for (int i = 0; i < T; i++) {
		string temp = words[i];
		bool index[26] = { false };
		bool groupWord = true;
		for (int j = 0; j < temp.length(); j++) {
			if (index[temp[j] - 'a'] == true) {
				groupWord = false;
			}
			if (temp[j] != temp[j + 1]) {
				index[temp[j] - 'a'] = true;
			}
		}
		if (groupWord == true) checker++;
	}
	cout << checker << endl;

	return 0;
}