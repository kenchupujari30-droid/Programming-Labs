#include <stdio.h>

int main() {
    int a, b;
    
    printf("Enter two integers (a b): ");
    scanf("%d %d", &a, &b);
    
    printf("\nResults:\n");
    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    
    if (b != 0) {
        printf("a / b = %d\n", a / b);
        printf("a %% b = %d\n", a % b);
    } else {
        printf("Cannot divide by zero!\n");
    }
    
    return 0;
}