# Unit 5.1 M4 Task 3
Why are out-of-place algorithms generally considered safer?

a) They only create additional variables that are O(1) space. 
b) Because they avoid side-effects.
c) They have an O(1) space cost.
d) They avoid the cost of initializing o0r copying data structures.

The answer is b) They avoid side-effects.

In contrast to in-place functions, out-of-place functions don't modify or destroy the input state when they are run. Any changes done to the input are done to a copy of the input, not the original that was passed in. This is why they are less space-efficient. If you have a list of 1,000,000 items that you want to square, you first have to make a copy of that list. Now, you have two lists of 1,000,000 items. 

However, you avoid any side-effects that might be unintended!