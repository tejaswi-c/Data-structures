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


6.Best time to buy and sell stocks
def maxProfit(self,prices):
	mini=float('inf')
	profit=0
	for i in prices:
		if i<mini:
			mini=i
		elif i-mini>profit:
			profit=i-mini
	return profit


7.Best time to buy and sell stocks II
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxprofit+=prices[i]-prices[i-1]
        return maxprofit
8.Jump game
def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest=0
        for i in range(len(nums)):
            if i>furthest:
                return False
            furthest=max(furthest,i+nums[i])
            if furthest>=len(nums)-1:
                return True 
        return False 
Algorithm            
#initialize the variable
#traverse array
#if the current index is greater than i 
#update the furthest with max value in previous value or i+nums[i]
#if furthest>=len(nums)-1 then return true
#else return false




9.Jump game-II
Approach-1:Greedy Algorithm 
1.Initialize two pointers-current max reach and next max reach 
2.iterate through the array 
3.current_max_reach-farthest index you can reach with current number of jumps
  next_max_reach-farthest index you can reach with an additional jump
4.current_max_reach 
5.continue till you reach the last index 



def jump(nums):
    n=len(nums)
    if n==1:
    	return 0
    jumps=0
    current_max_reach=nums[0]
    next_max_reach=nums[0]
    for i in range(1,n):
    if i>current_max_reach:
    	jumps+=1
    	current_max_reach=next_max_reach
    next_max_reach=max(next_max_reach,i+nums[i])
    return jumps 


10.H-Index

We then iterate through the sorted array and for each citation count, 
we compare it to the number of remaining elements in the array.
def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        n=len(citations)
        h=0
        for i in range(n):
            if citations[i]>=i+1:
                h=i+1
        return h

11.Insert Delete GetRandom
class RandomizedSet(object):
    def __init__(self):
        self.list=[]
        self.set={}
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.list:
            self.list.append(val)
            return True
        return False
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            self.list.remove(val)
            return True
        return False
    def getRandom(self):
        return random.choice(self.list)



12.Product of Array Except Self 
def productExceptSelf(self, nums):
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]
        result = [prefix_products[i] * suffix_products[i] for i in range(n)]
        return result
# Initialize arrays to store prefix and suffix products
# Compute prefix products
# Compute suffix products
# Compute the final result by multiplying prefix and suffix products


13.Candy
 def candy(self, ratings):
        #ratings are sorted out
        #atleast one candy 
        #as the ratings increases allocates some more condies#formuls/logic 

        n=len(ratings)
        candies=[1]*n 
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(n-2,-1,-1):
            if  ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)

        total_candies=sum(candies)
        return total_candies
	 
