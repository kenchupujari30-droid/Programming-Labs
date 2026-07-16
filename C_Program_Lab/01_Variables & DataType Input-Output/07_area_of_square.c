#include <stdio.h>

int main()
{
  int side;
  printf("Please enter the area of the squre in cms: ");
  scanf("%d", &side);
  printf("The area of your square is %d cm*cm",side*side);
}

// $ gcc 07_area_of_square.c -o program.exe && ./program.exe && rm program.exe
// Please enter the area of the squre in cms: 10
// The area of your square is 100 cm*cm(my-first-python-project) 