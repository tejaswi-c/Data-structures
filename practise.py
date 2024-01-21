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

5.Merge sorted array




Algorithm:
-Traverse from right to left 
-create two pointers for first array and one for second
 -loop:
    if element of first array is greater then add it to first array
    else add it to the next array.
-add remaining elements in the second array
def merge(self, nums1, m, nums2, n):
        p1=m-1
        p2=n-1
        k=m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[k]=nums1[p1]
                p1-=1
            else:
                nums1[k]=nums2[p2]
                p2-=1
            k-=1
        if p2>=0:
            nums1[:k+1]=nums2[:p2+1]





Leetcode top Interview 150
2.Remove elements
                                            
Algorithm 
-count value s                                           
-traverse 
-remove first occurance of val
                                       
def removeElement(self, nums, val):
         s=nums.count(val)
        for i in range(s):
            nums.remove(val)
                    
       
        return len(nums)




3.Remove duplicates from the sorted array
 def removeDuplicates(self, nums):
    
        duplicates=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                duplicates+=1
            else:
                nums[i-duplicates]=nums[i]
        return len(nums)-duplicates
                                           




4.Remove duplicates from sorted array-II
 def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k   


5.Rotate array 
def rotate(nums, k):
        n = len(nums)
        k = k % n
        def reverse(s,e):
            while s<e:
                nums[s],nums[e]=nums[e],nums[s]
                s+=1
                e-=1
        reverse(0,n-1)  #complete rotate
        reverse(0,k-1)  #first part rotate
        reverse(k,n-1)  #second part rotate 
        
