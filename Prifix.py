strs=list(map(str,input().split(",")))
strs.sort();    
first = strs[0]
last = strs[-1]
prefix = ""
for i in range(len(first)):
    if i < len(last) and first[i] == last[i]:
        prefix += first[i]
    else:
        break
print("Longest prefix : ",prefix);