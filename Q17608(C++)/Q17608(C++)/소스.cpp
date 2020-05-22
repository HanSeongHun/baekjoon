#include<iostream>
#include<vector>
using namespace std;

vector<int> make_blocks(int a) {
	vector<int> blocks;
	for (int i = 0; i < a; i++) {
		int temp = 0;
		cin >> temp;
		blocks.push_back(temp);
	}
	return blocks;
}

int main() {
	int a = 0;
	int can_see = 1;
	cin >> a;
	vector<int> blocks = make_blocks(a);
	int last = blocks.back();
	int size = blocks.size();
	for (int i = 0; i < size; i++) {
		int temp = 0;
		temp = blocks.back();
		if(last < temp) {
			can_see++;
			last = temp;
		}
		blocks.pop_back();
	}

	cout << can_see;
}