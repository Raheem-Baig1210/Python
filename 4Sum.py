def fourSum(nums, target):
    l1=[]
    l2=[]
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k]+nums[l])==target:
                        l2.append(nums[i])
                        l2.append(nums[j])
                        l2.append(nums[k])
                        l2.append(nums[l])
                        l2.sort()
                        if (l2 in l1) or (len(l2)>4):
                            pass
                        else:
                            l1.append(l2)
                            l2=[]
    return l1
nums=[-2,-1,-1,1,1,2,2]
target=0
print(fourSum(nums,target))