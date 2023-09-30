# write a program to Count the Frequency of the word appearing in a string.
#steps: store string words in a variable,make split that list,empty dictionary,for loop for word in d.key:
def Freq_Words():
    str = input("Enter the String to Find out Frequency: ")
    Li = str.split()
    # print(Li)
    d ={}
    for word in Li:
        if word not in d.keys():
            d[word] = 0
        d[word] += 1
    print(d)


Freq_Words()
