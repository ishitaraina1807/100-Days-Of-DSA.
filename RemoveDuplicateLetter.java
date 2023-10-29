public class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26]; 

        for (char c : s.toCharArray()) {
            count[c - 'a']++; 
        }

        StringBuilder result = new StringBuilder();
        boolean[] added = new boolean[26]; 

        for (char c : s.toCharArray()) {
            count[c - 'a']--; 
            if (added[c - 'a']) {
                continue; // Skip characters that are already added to the result
            }

            // Remove characters from the result while they are larger and still available
            while (result.length() > 0 && c < result.charAt(result.length() - 1) && count[result.charAt(result.length() - 1) - 'a'] > 0) {
                added[result.charAt(result.length() - 1) - 'a'] = false;
                result.deleteCharAt(result.length() - 1);
            }

            result.append(c); 
            added[c - 'a'] = true;
        }
     return result.toString();
    }

}
