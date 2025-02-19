def threeSum(nums):
    l1=[]
    l2=[]
    # if nums==[0,0,0]:
    #     return [[0,0,0]]
    for i in range(len(nums)):
        for j in range (i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if (nums[i]+nums[j]+nums[k])==0:
                    l2.append(nums[i])
                    l2.append(nums[j])
                    l2.append(nums[k])
                    l2.sort()
                    if l2 in l1:
                        pass
                    else:
                        l1.append(l2)
                    l2=[]
    return l1
nums=[-1,-2,0,1,2]
print(threeSum(nums))