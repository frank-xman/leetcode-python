class Solution(object):
	#python2 has object and python3 is better than 2 in class sus
	def Min(self,s):
		tim=sorted(map(lambda t:int( t[:2])*60+int(t[3:]) , s))
		return min((x-y)%24*60 for x ,y in zip(tim[1:]+tim[:1],tim))#错位相减
