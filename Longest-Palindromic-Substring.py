class Solution(object):
	def longestPalindrome(self,s):
		if len(s)<=1:
			return s
		else:
			start,end=self.dplong(s,0,len(s))
			return s[start:end]
	def dplong(self,s,start,end):
		maxlen=1#一个字母算作是它单独的回文，这里作是为了方便
		for i in xrange(end):
			if i-maxlen>=1 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]:
			#这里是不从开头算起，所以要多减去1，而且避免了比从开头段的情况
				start=i-maxlen-1
				maxlen+=2#对称结构所以加2
			if i-maxlen>=0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]:
				start=i-maxlen
				maxlen+=1#从开头算起只加1
		return start,start+maxlen
