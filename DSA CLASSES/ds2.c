#include <stdio.h>
#include <time.h>
// perform the bubble sort
void bubbleSort(int array[], int size) {



 // loop to access each array element
  for (int step = 0; step < size - 1; ++step) {
      
    // loop to compare array elements
    for (int i = 0; i < size - step - 1; ++i) {
      
      // compare two adjacent elements
      // change > to < to sort in descending order
      if (array[i] > array[i + 1]) {
        
        // swapping occurs if elements
        // are not in the intended order
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}



// print array
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
}


int main() {
  int size ,  data[2000],i=0;
  printf(“ Array size =”);
  scanf("%d",&size);
for(i=0;i<size;i++)
data[i]=rand();
     // Calculate the time taken by fun()
    clock_t t;
    t = clock();
    bubbleSort(data, size);  
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    printf("bubble_sort() took %f seconds to execute \n", time_taken);
    //return 0;




  
  printf("Sorted Array in Ascending Order:\n");
  printArray(data, size);
}