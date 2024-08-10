# write a for loop to print numbers from 1 to 10
'''for i in range(1,11):
   print(i,)'''
# write a for loop to iterate through a list of fruits (['apple','banana','cherry','date'])and print each fruit
'''fruits=['apple','banana','cherry','date']
for f in fruits:
   print(f)'''
# write a for loop to calculate and print the factorial of a given number
'''n=int(input('Enter a number:'))
factorial=1
for i in range(1,n+1):
   factorial*=i
   print(f'factorial of {n} is {factorial}')'''
#write a for loop to print the multiplication table 5
'''n=int(input('enter a table number:'))
for i in range(1,11,1):
   print(f'{n} x {i} = {n*i}')'''
#write a for loop over write a dictionary of students and grade
'''std_grade={'Alice': 85, 'bob': 78,'charlie': 92}
for student, grade in std_grade.items():
   print(f'{student}: {grade}') '''
# sum of even numbers 1 to 100 numbers 
'''sum=0
for num in range(1,101):
   if num%2==0:
      sum=sum+num 
      print(f'The sum of even number 1 to 100 is {sum}')'''
#fibonacci sequence with first 10 elements
'''a=0
b=1
for i in range(10):
   c=a+b
   a=b
   b=c
   print(c,end=' ')'''
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(7))
#write a for loop to count the number of vowels present in a given string
'''string ='narasimha'
vowels ='aeiouAEIOU'
count = sum(string.count(vowel) for vowel in vowels)  
print(count)'''
'''sentence = input('enter a sentence:')
string = sentence.lower()
count = 0
list1 = ['a','e','i','o','u']
for char in string:
    if char in list1:
        count = count+1
print(f'number of vowels :{count}')'''
#
'''string = input('enter a sentence:')
up=string.upper()
print(up)'''
'''input= ['narasimha','rohiT','Kohili']
lst=[x.upper() for x in input]
print([lst]) '''
#qudratic eqution
'''import cmath
a=29
b=4
c=1
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print(sol1,sol2)'''
#armstrong number
num=int(input('enter a number: '))
order=len(str(num))
sum=0
temp=num
while(num>0):
    r=num%10
    sum=sum+r**order
    num=num//10
if (temp==sum):
    print('armstrong')
else:
    print('nor an armstrong')        




