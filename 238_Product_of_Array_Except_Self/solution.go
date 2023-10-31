/*

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

*/

/*

approach:

1. Iterate through the array, res[I] = res[I] * prefix
    1. prefix = prefix * nums[I], as we need to multiply previous numbers without that number, so will do the multiplication in the res[I] first then the prefix will be updated
2. iterate through the array, res[I] = res[I] * postfix [Note: this time from last to first]
    1. postfix = postfix * nums[I]  as we need to multiply previous numbers without that number, so will do the multiplication in the res[I] first then postfix will be updated

## DRY RUN:

nums = [1,2,3,4]

res = [1, 1, 1, 1]

**`Output:** [24,12,8,6]`

prefix = 1, postfix = 1

for I = 0 to len(nums):

I = 0:

res[0] = res[0] * prefix —>     1 * 1 = 1

prefix = prefix * nums[0] —>  1 * 1 = 1

I = 1:

res[1] = res[1] * prefix —>     1 * 1 = 1

prefix = prefix * nums[2] —>  1 * 2 = 2

I = 2:

res[2] = res[2] * prefix —>     1*  2 = 2

prefix = prefix * nums[2] —>  2 * 3 = 6

I = 3:

res[3] = res[3] * prefix —>     1 * 6 = 6

prefix = prefix * nums[3] —>  6 * 3 = 18 // No use after that so Chill !!

Res = [1 , 1, 2, 6]

For I = 3 to 0:

     I= 3:

     res[3] = res[3] * postfix       —>     6 * 1 = 6

postfix = postfix * nums[3]  —>     1 * 4 = 4

I = 2

res[2] = res[2] * postfix       —>     2 * 4 = 8

postfix = postfix * nums[2]  —>     4 * 3 = 12

I= 1

res[1] = res[1] * postfix       —>     1 * 12 = 12

postfix = postfix * nums[1]  —>     12 * 2 = 24

I= 0

res[0] = res[0] * postfix       —>     1 * 24 = 24

postfix = postfix * nums[1]  —>     24 * 1 = 24 // No use after that so Chill !!

Res = [24, 12, 8, 6]

*/

func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    for i := 0; i < len(nums); i++ {
        res[i] = 1
    }
    prefix:= 1
    postfix:=1

    for i := 0; i < len(res); i++{
        res[i] = res[i] * prefix
        prefix = prefix * nums[i]
    }

    for i := len(res)-1; i>= 0; i--{
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]
    }
    return res
}
