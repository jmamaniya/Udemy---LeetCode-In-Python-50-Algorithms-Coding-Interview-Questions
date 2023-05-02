# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans

        for i in range(1, n + 2):
            first = first.next

        while (first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next

s = Solution()
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

answer = s.removeNthFromEnd(node_1, 1)
# print(answer.val)

while(answer!=None):
    print(answer.val)
    answer = answer.next