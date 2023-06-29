Searching and sorting
7.Majority element
 -A majority element in an array A[] of size n is an element that appears 
 more than n/2 times (and hence there is at most one such element). 

Examples : 
Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater than the 
half of the size of the array size. 

Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is greater than 
the half of the size of the array size.

App1:create a dictionary
-calculate the count for each value in array
-check if the count of any number is greater than n/2
-return it else return -1

def majority(nums):
    num_map={}
    for i in nums:
        if i not in num_map:
            nummap[i]=1
        else:
            num_map[i]+=1
    for i in num_map:
        if num_map[i]>len(nums)/2:
            return i
    return -1

TC:O(n)
SC:O(n)

App2:use Boyre Moore Majority Vote algorithm
-traverse the list
-if next element is same inc count else dec count
-if count=0 update candidate to i inc count
-again traverse find count of candidate
-if it is >n/2 return candidate else majority not found
def majority(nums):
    candidate=None
    count=0
    for i in nums:
        if num=candidate:
            count+=1
        else:
            count-=1
        if count==0:
            candidate=i
            count=1
    for num in nums:
        if num==candidate:
            frequency+=1
    if frequency>len(nums)/2:
        return candidate
    else:
        return "No majority element"
TC:O(n)
SC:O(1)

8.Count triplets with sum smaller than a given values
App1:find all the possible combinations
-count the no. of combinations having sum of triplets greater
 than sum
-return count
App2:Two pointer approach
-sort the array
-iterate i to third to last element
-use left and right
  If the sum is less than the target, then all the elements
  between 'left' and 'right will also form a valid triplet
  with the current 'i' and 'right'.


def countTriplets(nums,target_sum):
    arr.sort()
    n=len(arr)
    count=0
    for i in range(n-2):
        left=i+1
        right=n-1
        while left<right:
            cur_sum=arr[i]+arr[left]+arr[right]
            if cur_sum<target_sum:
                count+=right-left
                left+=1
            else:
                right-=1
    return count
TC:O(n^2)
SC:O(1)

9.Maximum Sum Subsequence with no adjacent elements
-use dynamic programming
TC:O(n)
SC:O(n)
  
10.Merge Sorted Arrays using O(1) Space
App:use merge sort-in place merging approach
-initialize m and n and i,j
-traverse with i and j in both arrays
-if num1[i]<=num2[j] inc i
-else insert at current position of i inc i and j
-also inc len of num1 by 1
-after loop,there may be remaining elements in nums2
-append those to the num1
def mergesortedarrays(num1,nums2):
    m=len(num1)
    n=len(num2)
    i,j=0,0
    while i<m and j<n:
        if num1[i]<=num2[j]:
            i+=1
        else:
            num1[i].insert(i,arr2[j])
            j+=1
            i+=1
            m+=1
    while j<n:
        arr1.append(arr2[j])
        j+=1

11.Inversion of array
12.Find Duplicates in O(n) Time and O(1) Extra Space 
App:create set
create a list to add duplicates
loop through the list
if num in found in set add to list else add to set
return dupliactes at the end
def duplicates(nums):
  dups=[]
  seen=set()
  for i in nums:
    if i in seen:
      dups.append(i)
    else:
      seen.add(i)
  return dups
TC:O(n)
SC:O(n)



    
 


