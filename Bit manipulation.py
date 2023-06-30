Bit manipulation is the process of manipulating individual bits within a binary representation of data.It involves performing operations on individual bits,such as
setting,clearing,lipping,computer programming,especially in low level sytem programming,cryptography,networking,optimization algorithms.

1.AND(&):
2.OR(|)
3.XOR(^)
4.NOT(~)
5.Leftshift(<<)
6.Rightshift(>>)

Easy:
1.count the number of set bits (1s) in a positive integer
def count_set_bits(n):
	count=0
	while n:
		n&=(n-1)
		count+=1
	return count
Ex:
n=43=101011
count=0
n=43&42=(101011&101010)=101010 count=1
n=42&41=(101010&101000)=101000 count=2
n=40&39=(101000&100111)=100000 count=3
n=32&31=(100000&11111)=000000 count=4
4 set  bits


2.Find the two non-repeating elements in an array of repeating elements

def find_single_element(nums):
	single_element=0
	for num in nums:
		single_element^=num
	return single_element
Ex:[2, 4, 3, 6, 4, 2, 3]
output=6
0^2=2
2^4=6
6^3=5
5^6=3
3^4=7
7^2=5
5^3=6

3.Program to find whether a no is power of two
def is_power_of_two(num):
	return n>0 and (n&(n-1))==0
Ex:
8-1000
7-0111
(8&7)=0000


4.Find position of the only set bit
Given a number N having only one ‘1’ and all other ’0’s in 
its binary representation, find position of the only set bit. 
If there are 0 or more than 1 set bit the answer should be -1.
 Position of  set bit 1 should be counted starting with 1
 from LSB side in binary representation of the number.
Ex:101011
-initialize position to 1
-create an array
-Iterate through the binary representation of the number N from right to left 
(from LSB to MSB):
-if n&1==1 append count to ans list
-right shift to move to next bit
-inc count
-follow conditiona specified in question and return
check if curren
def position_bits(n):
	position=1
	ans=[]
	while n!=0:
		if n&1==1:
			ans.append(count)
		n=n>>1
		count+=1
	if len(ans) or len(ans)>1:
		return -1
    return ans[0]

Ex:
100101-right most bit=1
10010-right shift
1001-return-1

5.Count number of bits to be flipped to convert A to B
-find xor of a and b
def countBitsFlip(a,b):
	c=a^b
	count=0
	while c:
		c&=(c-1)   
		count+=1
	return count
Ex:
A=1010=10
B=10100=20
C=A^B =11110=30
output=4
