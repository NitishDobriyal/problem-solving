
def anagram_checker(str_1,str_2):
    lst1 = [0]*26

    lst2 = [0]*26

    for char in str_1:
        lst1[ord(char)-97]+=1

    for char in str_2:
        lst2[ord(char)-97]+=1    


    if(lst1==lst2):
        return True
    else:
        return False

str_1 = "abcdj"
str_2 = "bdacj"

print(anagram_checker(str_1,str_2))