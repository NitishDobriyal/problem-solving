

def check_rotated_strings(s1,s2):
    temp = ''
    temp = s1+s1
    print(temp)

    #temp = 'abbaabba'
    #s2   = 'baab'

    for i in range(len(temp)):
        match = 0
        if(temp[i]==s2[0]):
            p=i
            q=0
            while(q<len(s2) and temp[p]==s2[q]):
                match+=1
                p+=1
                q+=1
        if(match == len(s2)):
            return True
    return False
    

s1 = 'abba'
s2 = 'baab'
print(check_rotated_strings(s1,s2))

#approach
'''
add s1+s2 in temp
and iterate in temp, check where temp[i]==s2[0]
wahan se while loop lgao till s2 length and count the matches, 
if matches length == s2 length: return True
otherwise false

'''
