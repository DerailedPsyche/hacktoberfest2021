

import java.util.ArrayList;

public class SelectionSort {
    static void selectionSort(int [] array){
        int small;
        int indexofsmall;
        int temp;
        for(int i=0;i<array.length-1;i++){
            indexofsmall=i;
            small=array[i];
            temp=small;
            for (int j=i;j<array.length-1;j++){
                if (array[j]<small){  //ressetting the small
                    small=array[j];
                    indexofsmall=j; //storing index of small

                }
            }

            array[i]=small; //swapping
            array[indexofsmall]=temp;
        }
        for (int i:
            array ) {
            System.out.println(i);
        }
    }
    public static void main(String[] args) {
        selectionSort(new int[]{5,2,3,1,8,0,10});
    }
}
