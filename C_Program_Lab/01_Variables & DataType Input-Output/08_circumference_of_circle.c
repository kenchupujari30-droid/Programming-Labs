#include <stdio.h>

int main()
{
  const float PI = 3.14159;
  int radius;

  printf("Please enter the radius of circle in cms: " );
  scanf("%d", &radius);
  printf("The circimference of yor circle is %f cm", 2 * PI *radius);

}

// $ gcc 08_circumference_of_circle.c -o program.exe && ./program.exe && rm program.exe
// Please enter the radius of circle in cms: 10
// The circimference of yor circle is 62.831802 cm(my-first-python-project) 