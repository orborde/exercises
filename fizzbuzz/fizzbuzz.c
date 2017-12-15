#include <stdio.h>

int main() {
	for (int i = 1; i <= 30; i++) {
		int printed = 0;
		if ((i%3) == 0) {
			printed = 1;
			printf("Fizz");
		}
		if ((i%5) == 0) {
			printed = 1;
			printf("Buzz");
		}

		if (!printed) {
			printf("%d", i);
		}

		putchar('\n');
	}
	return 0;
}
