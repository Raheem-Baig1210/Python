
def findMedianSortedArrays(nums1, nums2):
    l3=nums1+nums2
    a=len(l3)/2
    l3.sort()
    print(l3)
    s=0
    if len(l3)%2==0:
        a=int(a)
        s=l3[a-1]+l3[a]
        return s / 2
    else:
        a=len(l3)//2
        return l3[a]
l1=[1,3]
l2=[2,4]
print(findMedianSortedArrays(l1,l2))