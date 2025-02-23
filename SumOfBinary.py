def addBinary(a, b):
    c=int(a,2)+int(b,2)
    binary=bin(c)[2:]
    return binary
i=(input("Enter the first Binary number : "))
j=(input("Enter the second Binary number : "))
print("The sum of",i,"and",j,"is : ",addBinary(i,j))