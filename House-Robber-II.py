class Solution:
	def helper(self,nums):
		nums=[0,0]+nums
		for i,n in enumerate(nums[2:],start=2):
			#跳两格的插入，防止报警（题目要求）
			nums[i]=max(num[i-2]+n,nums[i-1)
			#挑选最大的
		return nums[-1]#返回最大的就是数组最后那个
	def rob(self,nums):
		if len(nums) ==1:
			return nums[0]
		return max(self.helper(nums[1:]),self.helper(nums[:-1]))

