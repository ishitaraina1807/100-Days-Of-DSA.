class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int x = target - nums[i];
            if (numMap.containsKey(x)) {
                return new int[]{numMap.get(x), i};
            }
            numMap.put(nums[i], i);
        }
        return null;
    }
}
