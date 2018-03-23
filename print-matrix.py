class Solution:
	def printMatrix(self,matrix):
		res=[]
		row=len(matrix)
		if row==0:
			return None
		col=len(matrix[0])
		left,top,right,bottom=0,0,col,row
		while (left<=right-1 and top<=bootom-1 ):
			for i in range(left,right):
				res.append(matrix[top][i])
				#left to the right
			for i in range(top+1,bootom):
				res.append(matrix[i][right-1])
				#top to bottom
			if top!=bottom-1:
				for i in range(right-2,ledt-1,-1):
					res.append(matrix[bottom-1][i])
			if left!=right:
				for i in range(bottom-2,top,-1):
					res.append(matrix[i][left])
			left+=1
			right-=1
			top+=1
			bottom-=1
		return res


