

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeSort {
    public List<Integer> mergeSort(List<Integer> array){
        List<Integer> left = array.subList(0, array.size() / 2); //cutting left half
        System.out.println("Splitting left: " + left);
        List<Integer> right = array.subList(array.size() / 2, array.size()); // cutting right half
        System.out.println("Splitting right: " + right);

        if(array.size()==1){
            return array;
        }

        return merge(mergeSort(left),mergeSort(right)); //this recursion split arrays to length 1 and merge them..then return merged array

    }

    private List<Integer> merge(List<Integer> left, List<Integer> right) {
        System.out.println("left"+left+"right"+right);
        List<Integer> sorted = new ArrayList<>();//creating a array for storing sorted array
        int r = 0;//right array index pointer
        int l = 0;//left array index pointer
        while (l < left.size() && r < right.size()) { //loop untill every element is traversed
            if (left.get(l) >= right.get(r)) {
                sorted.add(right.get(r)); //adding r th element on right to sorted list
                r++;
            } else {
                sorted.add(left.get(l)); //adding l th element on left to sorted list
                l++;
            }
        }
        sorted.addAll(left.subList(l, left.size())); //Merging all "leftovers" elements as is because we know they are sorted
        sorted.addAll(right.subList(r, right.size())); //Same
        return sorted;
    }

    public static void main(String[] args) {
        MergeSort sort =new MergeSort();
        List<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(2);
        list.add(3);
        list.add(1);
        list.add(8);
        list.add(0);
        list.add(2);
        list.add(10);
        list.add(100);
        System.out.println(sort.mergeSort(list));
    }
}
