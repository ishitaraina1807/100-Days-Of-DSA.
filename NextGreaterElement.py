def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n 
    stack = []

    for i in range(n):
        
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop() 
            result[index] = nums[i]  
        stack.append(i)

    return result

nums = [4, 1, 2, 25]
result = next_greater_element(nums)
print(result)
