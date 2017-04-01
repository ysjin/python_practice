#include "stdio.h"

// iterative
int fibonacci (int in) {
  int fib[2] = {0, 1};

  for (int i=2; i<=in; ++i) {
    fib[i%2] = fib[0] + fib[1];
        //printf("%d\n", fib[i%2]);      
  }
    
  if(in%2==0)
    return fib[0];
  else
    return fib[1];
}

int main() {
  printf ("%d\n", fibonacci(7));
}
