#include <stdio.h>

int x;

void fa() {
  x = x + x + 2;
}

int y = 3;

void fb() {
  x = 5;
  y = -2;
  fa();
}

void main() {
  fb();
  printf("x = %0d\n", x);
  printf("y = %0d\n", y);
  return 0;
}
