"""
You are given a non-empty array that represents the digits of a non-negative integer.
Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is 
at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).
- iterate over the list from the last item to the first item
  - check if the digit is a nine
    - set the current digit to zero
  - otherwise
    - add one to the current digit
    - return the input to the caller
prepend [1] to the start of the input list
Example 1:
Input: [1,3,3]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
Example 2:
Input: [3,2,2,0]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
Example 3:
Input: [0,0,0]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
# Space Complexity => O(1)
# Time Complexity => O(n)


def plus_one(digits):  # O(n)
    n = len(digits)  # O(1)
    for i in range(n):  # O(n)
        idx = n - 1 - i  # O(1)

        if digits[idx] == 9:  # O(1)
            digits[idx] = 0  # O(1)
        else:  # O(1)
            digits[idx] += 1  # O(1)
            return digits  # O(1)

    return [1] + digits  # O(1) / O(n) under the hood


#  0  1  2
# [1, 2, 3]

# n = 3
# i = 2
# idx = 3 - 1 - i


# Tests
print(plus_one([1, 3, 2]))  # [1,3,3]
print(plus_one([3, 2, 1, 9]))  # [3,2,2,0]
print(plus_one([9, 9, 9]))  # [1,0,0,0]
