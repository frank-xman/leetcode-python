'''
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
'''
class Solution:
	def delnote(self,listnote):
		d=ListNode(-1)
		d.next=listnode
		pre=d
		cur=listnode
		while cur:
			if cur.next and cur.next.val==cur.val:
				tmp=cur.next
				while tmp and tmp.val==cur.val:
					tmp=tmp.next
				pre.next=tmp
				cur=tmp
			else:
				pre=cur
				cur=cur.next
		return d.next
#删除重复的节点，并且不保留
