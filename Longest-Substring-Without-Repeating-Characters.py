class Solution(object):
	def lengthOfLongestSubstring(self, s):
		if len(s)<=1:
			return len(s)
		start,maxlen=0,0
		d={}
		for i in xrange(len(s)):#用xrange会比range 快很多，生成器
			if s[i] in d and start<=d[s[i]]:
					start=d[s[i]]+1
			else:
				maxlen=max(maxlen,i-start+1)
			d[s[i]]=i
		return maxlen
