package Algortithms.Searching;

public class BinarySearch {
    public static void binarySearch(int [] array,int key){
        int low=0;
        int high=array.length-1;
        int mid;
        while (low<high){
            mid=(low+high)/2;
            if(array[mid]==key){
                System.out.println("item found at index:"+mid);
                break;
            }
            else if(array[mid]>key){
                high=mid-1;
            }
            else low=mid+1;
        }
    }

    public static void main(String[] args) {
        binarySearch(new int []{1,2,4,6,8,10,12},10);
    }
}
