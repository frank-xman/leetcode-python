class Solution(object):
    def optimalDivision(self, nums):
        A=map(str,nums)
        if len(A)>2:
            A[1]='('+A[1]
            A[-1]+=')'
            
        return '/'.join(A)
        """
        :type nums: List[int]
        :rtype: str
        """
