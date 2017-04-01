#include "stdio.h"

// recursive
int bsearch_rec(int sorted_arr[], int start, int end, int key) {
  if (end >= start)
  {
    int mid = start + (end-start)/2;
    //printf("%d\n", mid);

    if (sorted_arr[mid] == key) {
      return mid;
    }
    else if(sorted_arr[mid] > key) {
      return bsearch (sorted_arr, start, mid-1, key);
    }
    else {
      return bsearch (sorted_arr, mid+1, end, key);
    }
  }

  return -1;
}

// iterative
int bsearch_it(int arr[], int start, int end, int key) {
  while (start <= end) {
    int mid = start + (end-start)/2;

    if (arr[mid] == key)
      return mid;
    else if (arr[mid] < key)
      start = mid + 1;
    else
      end = mid - 1;
  }

  return -1;
}

int main() {
  int sorted_arr[] = {2, 3, 5, 7, 9, 10, 15, 19};

  printf("%d\n", bsearch_it(sorted_arr, 0, 7, 10)); 

  return 0;
}



