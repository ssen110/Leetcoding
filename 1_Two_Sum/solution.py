'''
Link: https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


'''

'''

Explanation and Dry Run:

    Approach:

as we observe, one solution will exist for sure, 

1. Iterate through the array and if the (target - nums[i]) is present in previous values that means we got the result 
2. Else, Just save the index into the dict

### DRY RUN:

[3,2,4, 5], target = 6

my_dict = {}

I = 0, value = 3

as (target - value) i.e. **(6 - 3) = 3**  is not in my_dict.keys():

add the key into my_dict, —> my_dict[3] = 0

I = 1, value = 2

(6-2) = 4  ****is not in my_dict.keys():

add the key into my_dict, —> my_dict[2] = 1

I = 2, value = 4

(6 - 4) = 2  is in my_dict.keys():

return (my_dict[target - nums[I], I) i.e. [1, 2]

'''



def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in my_dict.keys():
                return [my_dict[target - nums[i]], i]
            my_dict[nums[i]] = i

        return [-1, -1]



