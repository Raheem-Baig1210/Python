def plusOne(digits):
    a=''
    for i in digits:
        b=str(i)
        a=a+b
    c=int(a)
    c=c+1
    a=str(c)
    l1=[]
    for i in a:
        b=int(i)
        l1.append(b)
    return l1
l1=list(map(int,input("Enter the elements of list : ").split(",")))
print("Increment of the given array is : ",plusOne(l1))