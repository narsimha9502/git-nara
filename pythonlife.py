'''#python program to checke if a number is positive or negetive
number=float(input('Enter a number:'))
if number>0:
    print('number is positive')
elif number<0:
    print('number is negetive')
else:
    print('zero')  '''
'''#find the number is even or odd
number = int(input('enter a number:'))
if number%2==0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')  '''
# python program to check leap year
'''def checkyear():
    year=int(input('enter year:'))
    if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
        print(f'{year} is leap year') 
    else:
        print(f'{year} is not leap year') 
checkyear()'''
# find the largest number
#list=(20,45,71)
#print(max(list)) 
'''number1=float(input('enter the number:'))
number2=float(input('enter the number:'))         
number3=float(input('enter the number:')) 

if number1>=number2 and number1>=number3:
    largest=number1
elif number2>=number1 and number2>=number3:
    largest=number2
else:
    largest=number3
print('largest number is:',largest)'''
# Find prime number
'''def prime_number(number):
    if number>1:
        for num in range(2,number):
            if number%2==0:
                return 'not prime'
        return "prime"
    return 'not prime'
print(prime_number(10)) '''
'''num=int(input('enter number:'))
if num>1:
    for i in range(2,num):
       if num%i==0:
        print('not prime')
    else:
        print('prime')'''
    


   