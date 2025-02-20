def lengthOfLongestSubstring(s):
    a=''
    c=0
    for i in s:
        if i in a:
            return c
        else:
            a=a+i
            c=c+1
s="abcabcabb"
print(lengthOfLongestSubstring(s))