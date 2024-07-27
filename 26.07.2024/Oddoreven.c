#include <stdio.h>

int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);

    if (number % 2 != 0) {
        printf("%d is odd.\n", number);
    } else {
        printf("%d is not odd.\n", number);
    }

    return 0;
}
