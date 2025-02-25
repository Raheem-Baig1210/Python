def twoSum(nums, target):
    s=0
    l1=[]
    l2=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                l1.append(i)
                l1.append(j)
                if l1 in l2:
                    pass
                else:
                    l2.append(l1)
                    l1=[]
    return l2
l1=list(map(int,input("Enter the elements of the list : ").split(',')))
b=int(input("Enter the target number : "))
print("The indexes of the elements whose sum is equal to targeted  number are : ",twoSum(l1,b))