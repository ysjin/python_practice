#include "stdio.h"

const int mat_size = 7;
typedef int Mat [mat_size][mat_size];

void swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

void swap_block() {

}

// poor locality
void transpose (Mat m, int size) {
  for (int r=0; r<size; r++) {
    for (int c=0; c<r+1; c++) {
      swap(m[r][c], m[c][r]);
    }
  }
}

// recursive
void transpose_rec (Mat m, int size) {
  if(size <= 4)
    transpose(m, size)
  else {
    transpose_rec (m, size/2);
    //
  }
}

// block
void transpose_block (Mat m, int size) {



}

void print_mat(Mat m) {
  for (int r=0; r<mat_size; r++) {
    for (int c=0; c<mat_size; c++) {
      printf("%3d ", m[r][c]);
    }
    printf("\n");
  }
}


int main () {
  Mat m = { { 0, 1, 2, 3, 4, 5, 6}, 
            { 7, 8, 9, 10, 11, 12, 13}, 
            { 14, 15, 16, 17, 18, 19, 20}, 
            { 21, 22, 23, 24, 25, 26, 27}, 
            { 28, 29, 30, 31, 32, 33, 34}, 
            { 35, 36, 37, 38, 39, 40, 41}, 
            { 42, 43, 44, 45, 46, 47, 48}  
  };

  print_mat (m) ;

  transpose(m);

  print_mat (m);
}
