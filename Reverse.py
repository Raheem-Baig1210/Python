def reverse(x):
    a=str(x)
    b=''
    for i in a:
        if i.isdigit():
            i=str(i)
            b=i+b
    if int(b) <= -2**31 or int(b)>=2**31-1:
        return 0
    if x<0:
        c=-int(b)
        return c
    c=int(b)
    return c
num=int(input("Enter any number to be reversed : "))
print("Reversed number is : ",reverse(num))