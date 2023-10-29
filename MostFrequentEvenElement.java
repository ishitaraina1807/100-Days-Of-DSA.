class Solution {
    public int mostFrequentEven(int[] nums) {
         Map<Integer, Integer> frequency = new HashMap<>();

        int mostFrequentEven = -1;
        int maxFrequency = 0;

        for (int num : nums) {
            if (num % 2 == 0) {  // Check if the number is even
                frequency.put(num, frequency.getOrDefault(num, 0) + 1);
                if (frequency.get(num) > maxFrequency || (frequency.get(num) == maxFrequency && num < mostFrequentEven)) {
                    mostFrequentEven = num;
                    maxFrequency = frequency.get(num);
                }
            }
        }

        return mostFrequentEven;
    }
}
