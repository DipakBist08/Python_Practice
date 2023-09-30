#write a program to find common letter from two string.
#string 1st = NAINA
#string 2nd =REENA
#steps:
#1>Remove Duplicate elements by using set
#2>extract common value form those unique elements.
def Find_Common_Letter():
    str1=input('Enter First String : ')
    str2=input('Enter Second String: ')
    s1=set(str1) #set will remove duplicate elements
    s2=set(str2)
    common_letter=s1 & s2 #& letter will extrect common letter form the string
    # print(s1) To check output
    # print(s2) To check output
    print(common_letter)
Find_Common_Letter()



