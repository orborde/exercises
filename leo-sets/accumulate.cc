#include <cassert>
#include <unistd.h> // lol
#include <iostream>
#include <unordered_map>
#include <set>
#include <string>

using namespace std;

int main() {
  unordered_map<string, set<int> > d;
  d.reserve(7000000);
  string line;
  while (getline(cin, line)) {
		assert(line.length() == 5);
		d[line].insert(d.size());

		if (d.size() % 100000 == 0) {
			cout << d.size() << endl;
		}
	}

	sleep(100000000);
}
