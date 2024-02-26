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


14.Trapping Rain water 

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6 units-count the units of water
	-measure y-axis height of each item

Approach:
	-keep track of maximum of left height for each height
	-keep track of maximum of right height for each height
	-traverse again
    -find waterlevel-min(max_left[i],max_right[i])
    -if waterlevel>heights[i] 
        then ith bar traps waterlevel-height[i]

Code:
    def trap(heights):
	    n=len(heights)
	    max_left,max_right=[0]*n,[0]*n

	    for i in range(1,n):
	        max_left[i]=max(max_left[i-1],heights[i-1])

	    for i in range(n-2,-1,-1):
	        max_right[i]=max(max_right[i+1],heights[i+1])

	    ans=0
	    for i in range(0,n):
	        water_level=min(max_left[i],max_right[i])
	        if water_level>heights[i]:
	            ans+=water_level-heights[i]
	    return ans

	heights=[0,1,0,2,1,0,1,3,2,1,2,1]
	x=trap(heights)
	print(x)

Time complexity:O(n)
Space complexity:O(n)


15.Roman to Integer
def romanToInt(self, s):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for char in s:
            current_value = roman_to_int[char]
            result += current_value
            if current_value > prev_value:
                result -= 2 * prev_value
            prev_value = current_value
        return result


16.Integer to Roman  
def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    result = ""
    
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]
    return result

    108-100 8  CV111

17.Length of last word
def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        count=0
        for i in range(n-1,-1,-1):
            if s[i]==' ':
                if count==0:
                    continue
                else:
                    return count
            count+=1
        return count

18.Longest Common Prefix
def longestCommonPrefix(self, strs):
	if not strs:
		    return ""
		prefix=strs[0]
		for string in strs[1:]:
		    while not string.startswith(prefix):
			prefix=prefix[:-1]
			if not prefix:
			    return ""
		return prefix  

19.Find the Index of the First Occurance in a string
def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len=len(needle)
        for i in range(len(haystack)):
            test=haystack[i:needle_len+i]
            if test==needle:
                return i
        return -1


20.Text Justification
Approach 
      #  traverse through each word
      #  find length of each word
      #   while length of word <maxwidth:
      #          append next word to current string
      #     add current string to result list
      # return the result list
      def fullJustify(self, words, maxWidth):
	      result=[]
	      current_string=''
	      for word in words:
	          if len(current_string)+len(word)<=max_width:
	              if current_string:
	                  current_string+=''+word 
	              else:
	                  current_string=word 
	          else:
	              result.append(current_string.ljust(max_width))
	              current_string=word 
	    if current_string:
	        result.append(current_string.ljust(max_width))
	    return result 
	      





