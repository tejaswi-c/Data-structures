
1.Minimum Window substring
Approach:
    -check if length of string s is less than string t
    -create a frequency map for characters in t
    -initialize the count,start,min_start=0,min_length=infinity
    -start,end points to first elements
    -traverse with end pointer
    -if char in s is present in map dec freguency,still if frequency>=0 inc count
    -if count=length(t) update min_length,min_start
    -to move start element inc frequency,dec count to move to next_window
    -return array of startletter to endletter
Code:
    def min_window(s,t):
        if len(s)<len(t):
            return ""
        map={}
        for char in t:
            if char in map:
                map[char]+=1
            else:
                map[char]=1
        count=0
        start=0
        min_length=float("inf")
        min_start=0
        for end in range(len(s)):
            if s[end] in map:
                map[s[end]]-=1
                if map[s[end]]>=0:
                    count+=1
        while count==len(t):
            if min_length>end-start+1:
                min_length=end-start+1
                min_start=start
            if s[start] in map:
                map[s[start]]+=1
                if map[s[start]]>0:
                    count-=1
            start+=1
        return "" if min_length==float("inf") else s[min_start:min_start+min_length]

    s="ADOBECODEBANC"
    t="ABC"
    x=min_window(s,t)
    print(x)    

output:
    BANC

timecomplexity:O(m+n)
spacecomplexity:O(m)

2.Boyer Moore Algorithm for Pattern Searching
Approach:
    1.preprocessing
    -create a function for badcharheuristic(string,size)
    -traverse through string - This loop fills the actual values of the last occurrence of characters in the pattern
    -returns the initialized bad character list.
    2.create a function for search(txt,pat)
    -m,n-stores the lengths of pattern and text
    -create badcharacter list for pattern
    -s=represents shift of pattern
    -while loop continues until pattern is fully searched
    -If the loop terminates with j becoming -1, it means that the pattern is present at the current shift s
    -We shift the pattern so that the next character in the text aligns with the last occurrence of it in the pattern. 
     If the pattern occurs at the end of the text, we shift by 1 to continue the search.
    -If the loop terminates with j not becoming -1, it means there was a mismatch between the pattern and the text at the current shift.
    -We shift the pattern so that the bad character in the text aligns with the last occurrence of it in the pattern.
     The max function ensures that we get a positive shift.
Code:
    def bad_char(string,size):
        badchar=[-1]*256
        for i in range(size):
            badchar[ord(string[i])]=i
        return badchar
    def search(txt,pat):
        m=len(pat)
        n=len(txt)
        badc=bad_char(pat,m)
        s=0
        while(s<=n-m):
            j=m-1
            while j>=0 and pat[j]==txt[s+j]:
                j-=1
            if j<0:
                print(f"pattern occur at shift {s}")
                s+=(m-badc[ord(txt[s+m])]) if s+m<n else 1
            else:
                s+=max(1,j-badc[ord(txt[s+j])])
    txt=  "AABAACAADAABAABA"
    pat=  "AABA"
    search(txt, pat)

output:
    pattern occur at shift 0
    pattern occur at shift 9
    pattern occur at shift 12

timecomplexity:O(m+n)
spacecomplexity:O(k)
k is the number of unique characters in the pattern. 


3.Rabin-Karp Algorithm for Pattern Searching
Approach:
-q is a prime number
-m,n-lengths of patterns,text
-i,j-iteration variables,p=0,t=0 -hash values for patterns and text
-h=1-hashvalue of pattern and text
-first loop -calculate h value
-The next two loops calculate the hash values of the pattern (p) and the first window of the text (t).
-rabin-karp rolling hash function is used
-if the pattern is found at the current index i,print
-After the comparison, the hash value of the next window in the text is calculated by subtracting the contribution of the first character in the current window
 and adding the contribution of the next character (txt[i+m]). This is done using the rolling hash technique.
-If the resulting hash value (t) becomes negative, it is adjusted to a positive value by adding q.
Code:
d=256
def search(txt,pat,q):
    m=len(pat)
    n=len(txt)
    i=0
    j=0
    p=0 # hash value for pattern
    t=0 # hash value for txt
    h=1
    for i in range(m-1):
        h=(h*d)%q
    for i in range(m):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(txt[i]))%q
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
            if j == m:
                print("Pattern found at index " + str(i))
        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q
            if t < 0:
                t = t+q
txt=  "AABAACAADAABAABA"
pat=  "AABA"
q = 101
search(txt, pat,q)

output:
pattern occur at shift 0
pattern occur at shift 9
pattern occur at shift 12
