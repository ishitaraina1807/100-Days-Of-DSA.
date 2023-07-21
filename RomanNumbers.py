class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0
        
        s = input()
        for letter in s:
            value = roman_values[letter]

            if prev_value < value:
                total -= 2 * prev_value

            total += value
            prev_value = value

        return total


