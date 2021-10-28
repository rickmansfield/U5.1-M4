# Unit 5.1 M4 Task 2
What is the time and space complexity of slicing an array in Python?

A) 
Time: O(1)
Space: O(n)

B)
Time:O(n)
Space:O(n)

C)
Time:O(1)
Space:O(1)

D)
Time:O(n)
Space:O(1)

Codesignal switches the order above. So look for the answer than contains ...

You might be wondering, what is the time and space complexity of slicing an array? To understand the complexity, you need to know what is happening behind the scenes when you take a slice of an array. First, you are actually allocating a new list. Second, you copy all of the items in your slice from the original array into the newly allocated list. This means that you have an O(n) time cost (for the copying) and an O(n) space cost for the newly allocated list.

You must keep these facts in mind and account for them when using a slice in your code. It's not a free operation.