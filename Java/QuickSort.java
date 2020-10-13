package Algortithms.Sorting;

import java.util.Arrays;
import java.util.List;

public class QuickSort {
    public Integer [] quickSort(Integer [] array,int left,int right) {
        int partitionIndex;
        int pivotIndex;
        if(left < right){
            System.out.println("partitioning from: "+left+"to: "+right);
           partitionIndex=partition(array, right,left,right);
            System.out.println("quick sort from :"+left+"to: "+(partitionIndex-1));
           quickSort(array,left,partitionIndex-1);
            System.out.println("quick sort from :"+(partitionIndex-1)+"to: "+right);
           quickSort(array,partitionIndex+1,right);
        }

        return array;
    }

//    private int partition(Integer [] array,int pivotIndex,int leftPointer,int rightPointer) { //used partition process
//        while (rightPointer>leftPointer) {
//            while (array[leftPointer] <= array[pivotIndex]) {
//                leftPointer++;
//            }
//
//            while (array[rightPointer] > array[pivotIndex]) {
//                rightPointer--;
//            }
//        if(leftPointer<rightPointer) {
//            swap(array, rightPointer, leftPointer);
//        }
//    }
//        swap(array,pivotIndex,rightPointer);
//        return rightPointer;
//    }

    private int partition(Integer [] array,int pivotIndex,int leftPointer,int rightPointer){
        int pivotValue =array[pivotIndex];
        int pointerSmallElement=leftPointer-1; //this variable holds the latest index value of group of elements which are less than pivot
        for (int i=leftPointer;i<rightPointer;i++){
            if(array[i]<pivotValue){ //if we found a value less than pivot lets swap it (to make it into small element group
                pointerSmallElement++;
                swap(array,i,pointerSmallElement);
            }

        }
        swap(array,rightPointer,pointerSmallElement+1); /*at this point we got our small group and large group..and pivot standing on right..lets swap pivot and
         pointer small element+1 ..so pivot will sit on its appropriate place*/
        return pointerSmallElement+1;
    }
    public void swap(Integer [] array,int index1,int index2){
        System.out.println("swaping "+array[index1]+"and"+array[index2]);
        int temp=array[index1];
        array[index1]=array[index2];
        array[index2]=temp;
    }


    public static void main(String[] args) {
    QuickSort sort = new QuickSort();
    Integer [] array= new Integer[]{10,16,8,2,9,12};
        System.out.println(Arrays.toString(sort.quickSort(array, 0, 5)));
    }
}
