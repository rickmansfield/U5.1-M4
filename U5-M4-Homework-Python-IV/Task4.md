# Unit 5.1 M4 Task4
In your own words, explain why the worst-case time cost of appending to a dynamic array is O(n)

Adding an item to an array is constant time (O(1)) in the average case. However, in the worst case, the cost is O(n) because the cost of copying the original items into the the array is O(n). If you consider appending and inserting to both be a form of "adding" to the array then there is a worst case O(n) factor. In other words.. When you insert into an array, all the items — starting at the index we are inserting into — have to be shifted one index. These items have to be "moved over" to make room for the new item being inserted. The worst-case scenario is inserting at the 0th index or array[0], and every item in the array has to shift over. Essentially you have "appended" to the "front" of the array at a cost of O(n)

## Reference
- [Link](https://lambdaschool.instructure.com/courses/1739/pages/objective-03-recall-the-time-and-space-complexity-the-strengths-and-weaknesses-and-basic-operations-of-a-dynamic-array?module_item_id=622153)