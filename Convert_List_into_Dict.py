#write a program to convert list into dictionary in python.

def ConvertListDictionary():
    list1=['Ram','Hari','Dipak','Bikram','Ananda']
    list2=[1,2,3,4,5]
    # print(type(list1))
    # print(type(list2))
    result=dict(zip(list2,list1))
    print(result)
ConvertListDictionary()
