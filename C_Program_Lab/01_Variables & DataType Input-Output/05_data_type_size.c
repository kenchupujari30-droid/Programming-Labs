#include <stdio.h>

int main()
{
  int integer;
  float decimal;
  double doub;
  char  character;

  printf("\n The size of int is %d bytes ", sizeof(integer));
  printf("\n The size of float is %d bytes ", sizeof(float));
  printf("\n The size of double is %d bytes ", sizeof(double));
  printf("\n The size of chatacter is %d bytes ", sizeof(char));
  
  return 0;
}

// $ gcc 05_data_type_size.c -o program.exe && ./program.exe && rm program.exe

//  The size of int is 4 bytes 
//  The size of float is 4 bytes 
//  The size of double is 8 bytes 
//  The size of chatacter is 1 bytes (my-first-python-project) 