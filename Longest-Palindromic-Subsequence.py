class Solution(object):
	def longest(self,s):
		n=len(s)
		if s[::-1]==s:
			return n
		dp=[[0 for _ in xrange(n) ] for __ in xrange(n)]
		dp[0][0]=1
		for i in xrange(1,n):
			dp[i][i]=1
			for j in xrange(j-1,-1,-1):
				if s[j]==s[i]:
					dp[i][j]=2+dp[i-1][j+1]
				else:
					dp[i][j]=max(dp[i-1][j],dp[i][j+1])
		return dp[n-1][0]
