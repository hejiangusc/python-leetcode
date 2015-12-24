class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		if l1 == None: return l2
		if l2 == None: return l1
		flag = 0
		dummy = ListNode(0); p = dummy
		while l1 and l2:
			p.next = ListNode((l1.val + l2.val + flag) % 10)
			flag = (l1.val + l2.val + flag) / 10
			l1 = l1.next; l2 = l2.next; p = p.next
		if l2:
			while l2:
				p.next = ListNode((l2.val + flag) % 10)
				flag = (l2.val + flag) / 10
				l2 = l2.next; p = p.next
		if l1:
			while l1:
				p.next = ListNode((l1.val + flag) % 10)
				flag = (l1.val + flag) / 10
				l1 = l1.next; p = p.next
		if flag == 1:
			p.next = ListNode(1)
		return dummy.next

#################### test case 1#################

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

test = Solution()
result = test.addTwoNumbers(l1, l2)
while result:
	print result.val
	result = result.next

print "-------------"

#################### test case 2#################

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(1)

test = Solution()
result = test.addTwoNumbers(l1, l2)
while result:
	print result.val
	result = result.next