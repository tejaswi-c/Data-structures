1.Linked list cycle

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next
            if slow==fast:
                return True
        return False

2.Remove Nth Node From End of List
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head 
        fast=slow=dummy
        for _ in range(n+1):
            fast=fast.next 
        while fast:
            slow=slow.next 
            fast=fast.next
        slow.next=slow.next.next 
        return dummy.next


3.Combinations
def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start,path):
            if len(path)==k:
                result.append(path[:])
                return 
            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        result=[]
        backtrack(1,[])
        return result 

4.permutations
def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        result=[]
        backtrack([])
        return result     
