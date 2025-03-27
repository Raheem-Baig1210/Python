
def findMedianSortedArrays(n1, n2):
    n3=n1+n2
    a=len(n3)
    n3.sort()
    if a%2==0:
        b=n3[a/2]
        m=float(n3[a/2]+n3[a/2 - 1])/2
        return m
    else:
        b=n3[a//2]
        m=b
        return m

n1=list(map(int,input("Enter the first array : ").split(",")))
n2=list(map(int,input("Enter the second array : ").split(",")))

print(findMedianSortedArrays(n1,n2))