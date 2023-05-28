# Write a function that takes in a list and returns the sum of all numbers in the list using recursion.
def recursive_sum(nums):
    if len(nums) == 0:
        return 0 
    return nums.pop() + recursive_sum(nums)

# test cases:
# nums = [1,2,3,7,8]
# nums = []
# nums = [-1]

# Write a function that computes the factorial of a number using recursion. The factorial of a
# number n is defined as the product of all numbers from 1 to n. For example, 4! = 4 x 3 x 2 x 1 = 24.
def recursive_factorial(num):
    if num <= 1:
        return 1
    return num * recursive_factorial(num-1)