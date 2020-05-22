#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool test(string f, string b) {
	int f_size = f.size();
	int b_size = b.size();
	
}


int result(string word) {
	int center = word.size() / 2;
	int size = word.size();
	string f_word;
	string b_word;
	if (word.size() % 2 == 0) {
		for (int i = 0; i < center; i++)
			f_word.push_back(word[i]);
		for (int i = center; i < size; i++)
			b_word.push_back(word[i]);
		if (f_word == b_word) {
			cout << "same";
			return 0;
		}
		else {
			string::iterator itr;
			for (itr = word.begin(); itr != word.end(); itr++) {
				cout << *itr << "  ";
			}
		}
	}
	return 0;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		cout << result(word);
	}
}