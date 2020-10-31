import java.util.HashMap;


public class SubArraySumEqualsK {
    /***calculating # of continuous subarray  that sum up to k*/

    public int subarraySum(int[] nums, int k) {
        int count = 0;
    
        HashMap<Integer, Integer> value_map = new HashMap<Integer,Integer>();
        value_map.put(0,1);
        
        int sum = 0;
        
        int a_length = nums.length;
        
        for(int i=0; i< a_length; i++){
            sum += nums[i];
            
            if(value_map.containsKey(sum-k))
                count += value_map.get(sum-k);
            value_map.put(sum, value_map.getOrDefault(sum, 0) +1);
        }
        return count;
              
        
    }

    public static void main(String[] args) {
        SubArraySumEqualsK sum = new SubArraySumEqualsK();
        int[] nums= {1,1,1};
        int k = 2;
        System.out.println("# of subarray that sum up to k is:" + sum.subarraySum(nums, k));


        
    }
    
}
