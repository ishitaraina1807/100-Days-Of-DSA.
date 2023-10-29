import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        
        // Define a recursive helper function to generate parentheses
        generate(result, "", 0, 0, n);
        
        return result;
    }
    
    private void generate(List<String> result, String current, int left, int right, int n) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }
        if (left < n) {
            generate(result, current + '(', left + 1, right, n);
        }
        if (right < left) {
            generate(result, current + ')', left, right + 1, n);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3;
        List<String> result = solution.generateParenthesis(n);
        for (String s : result) {
            System.out.println(s);
        }
    }
}
