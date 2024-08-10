#print hello world 
'''print('hello world')'''
#add two numbers
'''n1=10.2
n2=110.2
sum = n1+n2
print(sum)'''
#find squre root value
'''num=int(input('enter a squre number: '))
print(num**0.5)'''
#anthor method of squre root
'''import math
squre=int(input('enetr a squre number:'))
print(math.sqrt(squre))'''
#area of triangle
'''a=float(input('enter a value:'))
b=float(input('enter b value:'))
c=float(input('enter c value:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)'''
#qudartic equtaion
'''import cmath
a=1
b=5
c=6
d=(b**2)-(4*a*c)
s1=(-b-cmath.sqrt(d))/(2*a)
s2=(-b+cmath.sqrt(d))/(2*a)
print(s1,s2)'''
#swap two variables
'''x=10
y=20
x,y=y,x
print('x',x,'y',y)'''
#Generate random value
import random
print(random.randint(0,20))
#convert kilometer to miles
'''kilometer = float(input('enter a kilometers: '))
f = 0.621371
miles = kilometer*f
print(f'{kilometer} kilometr is equal to {miles} miles')'''
#convert temperature to fahrenheit
'''user=float(input('enter temperaturevalue:'))
f=(user*1.8)+32
print(f'{user} temperatuer of ferenhetih is{f}')'''
#Check if number is positive,negetive or zero
'''number=int(input('enter a number: '))
if number>0:
    print(f'{number} is positive number')
elif number==0:
    print('number is zero')
else:
    print('negetive number..')  '''
#Check even or odd
'''number=int(input('enter a number: '))
if (number%2)==0:
    print(f'{number} is even..')
else:
    print(f'{number} is odd..') '''
#Check leap year
'''year=int(input('enter a year: '))
if (year % 400 == 0) and (year % 100 ==0):
    print(f'{year} is leap year')
elif (year % 4 ==0) and (year % 100 !=0):
    print(f'{year} is leap year..')
else:
    print(f'{year} is not a leap year..') '''
#Find the largest among three numbers
'''num1=10
num2=20
num3=1
if (num1>=num2) and (num1>=num3):
    large=num1
elif (num2>=num1) and (num2>=num3):
    large=num2
else:
    large=num3
print('the large number is',large) '''
#another method
'''number=map(int,input('enter numbers: ').split(','))
large=max(number)
print(large)''' 
#Check prime number
'''number=int(input('enter a numbe: '))
if number==1:
    print('is not a prime number')
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, 'is not a prime')
            break
        else:
            print(number,'is a prime') '''
#print all prime number with in interval
'''first=100
last=199
for num in range(first,last+1):
    if num>1:
        for i in range(2,num):
            if (num%2)==0:
                break
            else:
                print(num)'''
#factorial
'''n=int(input('enter a factorial number:'))
if (n<0):
    print('invalid number..')
elif(n==0):
    print('factorial of o is 1..')
else:
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    print(f'factorial of {n} is {fac}')  '''  
# display multiplication table
'''t=int(input('enter a table number: '))
for i in range(1,11):
    print(t,'x',i,'=',t*i)'''
#armstong number
'''n=int(input('enter a number: '))
sum=0
t=n
while t>0:
    d=t%10
    sum=sum+d**3
    t=t//10
if n==sum:
    print(n,'is a armstrong') 
else:
    print(n,'is not a armstrong') '''
#sum of natural numbers
'''num=int(input('enter a number: '))
if num<0:
    print('enter a positive number..')
else:
    sum=0
    while(num>0):
        sum =sum+num
        num=num-1
    print(sum) '''
#find numbers divisable by another number
'''my_list=[12,16,19,25,260,299,417,521]
result=list(filter(lambda x:(x%2==0),my_list)) 
print('numbers divisable by 2 are',result)'''
#convert decimal to binary,octal,hexadecimal
'''num=3152567
print(f'the decimal value of {num} is:')
print(bin(num),'in binary.')
print(oct(num),'in octal.')
print(hex(num),'in hexadecimal.') '''
#find asscii values of character
'''name='n'
print('ascii value is :',ord(name))'''          

   



