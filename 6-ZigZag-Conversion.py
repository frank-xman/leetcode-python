class Solution(object):
		def convert(self,s,numRows):
				if numRows==1 or len(s)<=numRows:
						return s
				tmp=['']*numRows
				index,step=0,1
				for x in s:
						tmp[index]+=x
						if index==0:
								step=1
						elif index==numRows-1:
								step=-1
						index+=step
				return ''.join(tmp)
