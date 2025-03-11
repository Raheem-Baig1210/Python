def myAtoi(s):
    a=''
    g=True
    for i in s:
        if i==' ':
            pass
        elif i.isnumeric():
            a=a+i
        elif i=='-':
            g=False
    a=int(a)
    if g==False:
        a=-a
        return a
    else:
        return a
my=input("Enter the input string : ")
print(myAtoi(my))
ss=myAtoi(my)
print(type(ss))