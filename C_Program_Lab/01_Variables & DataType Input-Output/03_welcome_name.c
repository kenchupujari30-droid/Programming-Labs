#include <stdio.h>

int main()
{
  char name[30];
  printf("Please enter your name:");
  scanf("%29s" , name);
  printf("Welcome %s to AK coding.", name);
  
  return 0;
}

// $ gcc 03_welcome_name.c -o 03_welcome_name.exe && ./03_welcome_name.exe && rm 03_welcome_name.exe
// Please enter your name:Kenchu
// Welcome Kenchu to AK coding.(my-first-python-project) 
