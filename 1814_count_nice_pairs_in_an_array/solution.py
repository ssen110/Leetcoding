'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109


Solution :
    Intuition:
        1. nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        2. it can be written as
            nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        3. so if we can store the (nums[i] - rev(nums[i])) as key and we can get how many entries are having nums[i] - rev(nums[i]) as same.
        4. Let say with sum = 15, the count = 3
            - in that case the pair will be n(n-1)/2 --> 3(3 - 1)/2 = 3
            - it is nothing but picking up a pair from 3 items.
    Approach
        1. iterate through the array and save the count of (nums[i] - rev(nums[i]))
        2. and then take the values from my_dict and add into the result
    Complexity
        Time complexity: O(n), as iterating through the list once
        Space complexity: O(n), as my_dict is the extra dictionary
'''

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        my_dict = defaultdict(int)
        for num in nums:
            rev_num = int(str(num)[::-1])
            key = num -rev_num
            my_dict[key] = my_dict[key] + 1

        for k, v in my_dict.items():
            c = (v*(v - 1)) / 2 # picking up 2 numbers from that pair who makes the sum as the same
            res += c

        return res  % (pow(10, 9) + 7)

