#include <stdio.h>

int main()
{
  int first, second;
  printf("Please enter the first number:  ");
  scanf("%d" , &first);
  printf("Now enter the second number:  ");
  scanf("%d" , &second);
  printf("the two numbers you entered are  %d and %d ",first, second);
  
  return 0;
}


// $ gcc 04_two_integer_number.c -o program.exe && ./program.exe && rm program.exe
// Please enter the first number:  10
// Now enter the second number:  20
// the two numbers you entered are  10 and 20 (my-first-python-project) 