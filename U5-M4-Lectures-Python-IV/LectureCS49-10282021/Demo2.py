"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.
If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, 
then you should return the left-most "pivot" index.
total_sum = 28
left_sum = 11
idx = 3
num = 6
right_sum => total_sum - left_sum - num
right_sum => 28 - 11 - 6
right_sum = 11
check if left sum == right sum
  return the current index
add num to left sum
Example 1:     0 1 2 3 4 5
Input: nums = [1,7,3,6,5,6] total -> 28
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

create a total sum variable set it to the sum of all numbers
create a left sum and set that to zero

iterate over all of the numbers extracting the number??? and the index???
  check if the left sum is equal to (the total sum minus the left sum minus the number)...
    return the current index to the caller
  
  increment the left sum by the current number

if we get here we did not find a pivot index, return -1 to the caller


"""


def pivot_index(nums):  # O(n) linear time complexity, O(n) linear space complexity
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):

        if left_sum == total_sum - left_sum - num:
            return i

        left_sum += num

    return -1


# test
print(pivot_index([1, 7, 3, 6, 5, 6]))  # -> 3
print(pivot_index([1, 2, 3]))  # -> -1
