#include <stdio.h>
int main()
{
 int first, second, temp; 
printf("Please enter the first number");
scanf("%d", &first);
printf("Please enter the second number");
scanf("%d", &second);

// Swapping
temp = first;
first = second;
second = temp;
printf("The value of first is %d and second is %d", first, second);
return 0;
}


// $ gcc 10_swap_two_numbers.c -o program.exe && ./program.exe && rm program.exe
// Please enter the first number 5
// Please enter the second number 90
// The value of first is 90 and second is 5(my-first-python-project) 
