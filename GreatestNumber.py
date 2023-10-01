def GreatestNumber():
    num1=int(input('Enter The First Number: '))
    num2=int(input('Enter The Second Number: '))
    num3=int(input('Enter The Third Number: '))
    if num1==num2==num3:
        print('All the numbers are equal.')

    elif num1>num2 and num1>num3:
        print(f'{num1} is greatest number.')
    elif num2>num1 and num2>num3:
        print(f'{num2} is greatest number.')
    elif num3>num1 and num3>num2:
        print(f'{num3} is greatest number.')
    else:
        print('Invalid Input.')

GreatestNumber()