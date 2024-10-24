def isPalindrome(num):
    '''
    Approach: Reverse the num and compare it with orig
    '''
    num1 = num
    rev = 0
    while(num1):
        rem = num1%10
        rev = rem+rev*10
        num1 = num1//10 
    print('rev',rev)
    if(num==rev):
        return True
    else:
        return False

num = 12221    
print(isPalindrome(num))