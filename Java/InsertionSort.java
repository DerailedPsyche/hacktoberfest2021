package Algortithms.Sorting;

import java.util.ArrayList;

public class InsertionSort {
    static public void insertionSort(ArrayList<Integer> list){
        int temp;
        if(list.get(0)>list.get(1)) { //checking if fist >second
            temp = list.get(0); //swaping them
            list.set(0, list.get(1));
            list.set(1, temp);
        }
        for(int i=1;i< list.size()-1;i++){ //starts from index 1
            if(list.get(i)>list.get(i+1)){ //checking index i+1 is smaller

                for(int j=i;j>=0;j--){ //placing i+1 in appropriate posistion
                    if(list.get(j)>list.get(j+1)){
                        temp=list.get(j);
                        list.set(j,list.get(j+1));
                        list.set(j+1,temp);
                    }
                }
            }
        }
        System.out.println(list);
    }
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(10);
        list.add(3);
        list.add(1);
        list.add(8);
        list.add(7);
        list.add(2);
        list.add(4);
        insertionSort(list);
    }
}


