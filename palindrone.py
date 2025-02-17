
def isPalindrome(x):
    x=str(x)
    a=x[::-1]
    if x==a:
        return True
    else:
        return False
    
print(isPalindrome(121))
