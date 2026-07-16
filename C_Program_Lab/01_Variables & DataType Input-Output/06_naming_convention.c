#include <stdio.h>
int main()
{
  char first_name[20] = "Kenchu";
  char last_name[20] = "India";
  int age = 40;

  printf("First name: %s, Second name: %s, Age: %d", first_name, last_name,age);

  return 0;
}

// $ gcc 06_naming_convention.c -o program.exe && ./program.exe && rm program.exe
// First name: Kenchu, Second name: India, Age: 40(my-first-python-project) 