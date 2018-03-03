class Solution(object):
		def simplifyPath(self,path):
				res=[]
				paths=path.split('/')
				for path in paths:
						if path=='..' and len(res)>0:
								res.pop()
						if path and path!='.'and path!='..':
								res.append(path)
				return '/'+'/'.join(res)
