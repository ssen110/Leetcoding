'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

'''
    Explanation:
        we can use two pointers to get the result, we have a start and end pointer. so we will
        check start and end and check whose value is bigger, who ever is having higher values 
        those value will be multiplied with (j-i) as this value will be the lenghth of the 
        rectangle.
            finally, res = max(res, area_calculated)

'''


def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i, j = 0, len(height) - 1

        while i<j:
            if height[i] < height[j]:
                temp_res = height[i] * (j-i)
                i += 1
            else:
                temp_res = height[j] * (j-i)
                j -= 1
            res = max(res, temp_res)
        return res


