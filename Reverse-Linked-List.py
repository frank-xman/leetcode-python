class Solution:
		def reverseList(self,head):
				pre=none
				while head:
						cur=head
						head=head.next
						cur.next=pre
						pre=cur
				return pre
