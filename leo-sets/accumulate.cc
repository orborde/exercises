#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main() {
  map<string, set<int> > d;
  string line;
  while (getline(cin, line)) {
		assert(line.length() == 5);
		d[line].insert(d.size());

		if (d.size() % 100000 == 0) {
			cout << d.size() << endl;
		}
	}

	while(1);
}
