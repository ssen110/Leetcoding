class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = -99999
        for k in range(2, n+1):
            div = n // k
            rem = n % k
            temp = pow(div+1, rem) * pow(div, k - rem)
            res = max(res, temp)
        return res
        
