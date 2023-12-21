Sliding window
DS-Arrays,Strings,HashMaps


1.Maximum Average Subarray
2.Sliding window maximum  
3.Number of subarrays of size k and average>=threshold




1.Maximum Average Subarray
App1:Sliding window-remove left element-add right element

def maxavgsubarray(nums,k):
	n=len(nums)
    window_sum=sum(nums[:k])
    max_avg=window_sum/k
    for i in range(k,n):
    	window_sum=nums[i]-nums[i-k]
    	cur_avg=window_sum/k
    	max_avg=max(max_avg,cur_avg)
    return max_avg



2.Sliding window maximum

def sliding_window_maximum(nums,k):
	result=[]
	max_index=0
	for i in range(len(nums)):
		if i-max_index>=k:
			max_index+=1
	    if nums[i]>nums[max_index]:
	    	max_index=i
	    if i>=k-1:
	    	result.append(nums[max_index])
	return result



3.Number of subarrays of size k and average>=threshold

def num_of_subarrays(arr,k,threshold):
	count=0
	window_sum=sum(arr[:k])
	for i in range(k,len(arr)):
		cur_avg=window_sum/k
		if cur_avg>=threshold:
			count+=1
		window_sum=arr[i]-arr[i-k]
	if window_sum/k>=threshold:
		count+=1
	return count
