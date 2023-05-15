Arrays.Hard

1.Maximum sum of subarray
Approach:
	-It can be found using kadanes algorithm
	-Kadanes Algorithm is a two-pointer approach
	-initialize max_so_far and max_ending_here with first element of array
	-max_so_far-keeps track of highest sum among the subarray
	-max_end_here-keeps track of max among current element and sum till now
	-start traversing from second element

Example:
	arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	max_so_far = max_ending_here = -2

	index=1  max_ending_here=1   max_so_far=1
	index=2  max_ending_here=-2  max_so_far=1
	index=3  max_ending_here=4   max_so_far=4
	index=4  max_ending_here=3   max_so_far=4
	index=5  max_ending_here=5   max_so_far=5
	index=6  max_ending_here=6   max_so_far=6
	index=7  max_ending_here=1   max_so_far=6
	index=8  max_ending_here=5   max_so_far=6

Code:
	def maxsum_subarr(nums):
	max_ending_here=max_so_far=nums[0]
	for i in range(1,len(nums)):
		max_ending_here=max(nums[i],max_ending_here+nums[i])
		max_so_far=max(max_so_far,max_ending_here)
	return max_so_far

	nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	x=maxsum_subarr(nums)
	print(x)

Timecomplexity:O(n)
Spacecomplexity:O(1)


2.Trapping Rain Water
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

3.Container With Most Water
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49 -area 
          -measure x-axis and y-axis

Approach:
	-find height*widths
	1.find water_in_container
	-consider 2 edges 
	    -height=min(edge2-edge1)
	    -width=edge2-edge1
	    -caluculate area
	    -keep track of max_area
	2.choose edges
      -be greedy-choose first and last
      -by doing this we get most width,if not the height too
      -check which edge is smaller and move that pointer
    
Code:
    def max_area(edges):
    n=len(edges)
    left,right=0,n-1
    area=1

    while left<right:

        width=right-left
        height=min(edges[left],edges[right])
        area=max(area,width*height)

        if edges[left]<edges[right]:
            left+=1
        else:
            right-=1

    return area

	heights= [1,8,6,2,5,4,8,3,7]
	x=max_area(heights)
	print(x)

Timecomplexity:O(n)
Spacecomplexity:O(1)

4.Given an Array of Numbers Arrange the Numbers
  to Form the Biggest Number
  Input:a = [54, 546, 548, 60]
  Output=6054854654

Approach
  -convert numbers into strings
  -concatenate each number by 3 times as to cover all the
    cases where the strings have upto 3 digits
  -sort the strings in descending order
  -join the strings and convert into integer.

Note:
  -concatenate each number by n number of times 
   n is the highest no. of digits in list

Code:
    def Biggest_num(nums):
	  	nums=[str(num) for num in nums]
	  	nums.sort(key=lambda x:x*3,reverse=True)
	  	return int(''.join(nums))

	nums=[54, 546, 548, 60]
	x=Biggest_num(nums)
	print(x)

Timecomplexity:O(logn)
Spacecomplexity:O(n)

5.Longest Subarray Sum Divisible K
Approach:
	Bruteforce
	-traverse through subarrays 
	-find sum of each subarrays
	-find remainder of each sum with k
	-keep track of length of subarray
	
Code:
	def longsum_subarr_k(nums,k):
		n=len(nums)
		max_len=0
		for i in range(0,n):
			sum_subarr=0
			for j in range(i+1,n):
				sum_subarr+=nums[j]
				if sum_subarr%k==0:
				   max_len=max(max_len,j-i)
		return max_len

	nums=[2, 7, 6, 1, 4, 5]
	n=longsum_subarr_k(nums,3)
	print(n)

Timecomplexity:O(n**2)
Space Spacecomplexity:O(1)

