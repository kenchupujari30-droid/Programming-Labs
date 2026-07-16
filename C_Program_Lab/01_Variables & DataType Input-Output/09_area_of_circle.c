#include <stdio.h>

int main()
{
  const float PI = 3.14159;
  int radius;

  printf("Please enter the radius of circle in cms: " );
  scanf("%d", &radius);
  printf("The area of yor circle is %f cm", PI * radius * radius);
  
  return 0;
}

// $ gcc 09_area_of_circle.c -o program.exe && ./program.exe && rm program.exe
// Please enter the radius of circle in cms: 5
// The area of yor circle is 78.539749 cm(my-first-python-project) 