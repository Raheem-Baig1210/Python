def numOfSubarrays(arr):
    count=0
    for i in range(len(arr)):
        b=0
        for j in range(i,len(arr)):
            b = b + arr[j] 
            if b % 2 == 1:
                count = count + 1
    return count
l1=list(map(int,input("Enter the elements of the list : ").split(",")))
print("Number of sub array with odd sum is  : ", numOfSubarrays(l1))