package Algortithms.Sorting;

public class BubbleSort {
    @Override
    public String toString() {
        return "BubbleSort{}";
    }

    public static void bubblesort(int [] array){
        for(int i=0;i< array.length;i++){


            for (int j=0;j<array.length-i-1;j++){
                if (array[j]>array[j+1]){
                    int temp =array[j];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                }
            }

        }
        for (int i:array
             ) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        bubblesort(new int []{2,5,1,2,4,8,6,10});
    }
}
