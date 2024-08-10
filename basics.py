#lists
"""num=[72,33,44,28,675,34]
print(num)"""
"""num = [72,33,44,28,675,34]
print(num[-2])"""
"""num=[72,33,44,28,675,34]
num.append(True)
print(num)"""
"""fruits=['apple','orange','mango']
fruits.insert(0,'grapes')
print(fruits)"""
#(a+b)2
'''a=int(input('enter number:'))
b=int(input('enter number:'))
sum=a**2+b**2+2*a*b
print(sum)'''
'''a='10,20,30'
print(a.split)'''
'''import datetime
current_date=datetime.date.today()
print('date',current_date.day)
print('month',current_date.month)
print('year',current_date.year)'''
'''v1,v2,v3=map(float,input('enter a value').split())
sum=v1+v2+v3
tax=sum*.18
print(tax)'''
'''val = 'narasimha'

print(val[2:5:2])'''
'''val = 'rama'
print(val.isalpha())'''
'''maths=int(input("Enter a maths marks:"))
phy=int(input("Enter a physics marks:"))
sci=int(input("Enter a science marks:"))
per=((maths+phy+sci)/100)*100
print(per)'''
'''a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
sum=(a**2+b**2+2*a*b)
print(sum)'''
'''val='10,0,20,10'
print(val.split(' '))'''
'''x=lambda a,b : a+b
print(x(5,5))'''
'''def robo():
    print("hi")
    robo()
robo()    '''
# factorial using recursive faction
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=fact(5) 
print(x) '''
# while loop
'''i=2
while(i<=30):
    print(i)
    i+=2
print("end of while loop..") '''
#for loop
'''for i in range(2,21,2):
    print(i)'''
#break
'''for i in range(1,8):
    if i==4:
        continue
    
    print(i) '''
'''my_dict={'narasimha':22,'ramesh':21,'raghu':23}
for key,value in my_dict.items():
    print(f"name:{key},age:{value}")'''

'''try:
    text="my name is narasimha.."
    coun=text.count("")  
    print(coun)
except FileNotFoundError:
    print("numbers are not allowed")  '''

# while loop
'''i=1
while i<=10:
    print(i)
    i+=1'''
'''i=0
while i<=10:
    print("hello world")
    i+=1'''
'''num =1234
reversed_num=0

while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print(reversed_num)'''
#oops
'''class Narasimha:
    print("the is a class..")
    def display(self):
        a=10
        b=20
        print(a,b) 
obj=Narasimha()
obj.display()  '''
'''class Mobile:
    def __init__(self,brand,ram,battary,camera,price):
        self.brand=brand
        self.ram=ram
        self.battary=battary
        self.camera=camera
        self.price=price
    def display(self):
        print("brand:",self.brand) 
        print("ram:",self.ram)
        print("battary:",self.battary)
        print("camera:",self.camera)
        print("price:",self.price)
        print("---------------------")
        
obj=Mobile("redmi","6GB","5000mah","50mp","25000")
obj.display()
obj1=Mobile("realme","6GB","5000mah","50mp","25000")
obj1.display()
obj2=Mobile("oneplus","6GB","5000mah","50mp","25000")
obj2.display()
obj3=Mobile("oppo","6GB","5000mah","50mp","25000")
obj3.display()'''
'''class narasimha:
    def __init__(self):
        print("narasimha")
    def display(self):
        print("naidu")
obj=narasimha() 
obj.display()'''
'''x=10
y=0
while x>0:
    y+=1
    x-=2
print(x,y) '''
'''for i in range(1,20):
    if i%2==0:
        print(i) '''
'''num=int(input("enter a number:"))
fac=1
number=num
while number>0:
    fac=fac*number
    number=number-1
print(fac)'''
'''num=int(input("enter a number:"))
if num%2==0:
    print('not a prime..')
elif num<1:
    print('enter a valid number')    
else:
    print('prime') '''
'''num=6
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print() '''
'''for i in range(1,10):
    if i==5:
        break
    print(i)  '''
'''def add(a,b):
    return a+b
r=add(3,4)+add(5,6)
print(r) '''
'''def calcuiate_average(lst):
    return sum(lst)/len(lst)
lst = [2,3,4,53,49,10]
average=calcuiate_average(lst)
print(average)'''
'''def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiple(x,y):
    return x*y
def division(x,y):
    if y !=0:
        return x/y
    else:
        return "error"
import basics
def main():
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))

    print(f"{num1} +{num2} = {basics.add(num1,num2)}")
    print(f"{num1} -{num2} = {basics.subtraction(num1,num2)}")
    print(f"{num1} *{num2} = {basics.multiple(num1,num2)}")
    print(f"{num1} /{num2} = {basics.division(num1,num2)}")
if __name__=="__main__":
    main()  '''
'''v1,v2,v3=map(int,input('enter a number').split(' '))
sum = v1+v2+v3
print(sum)'''
'''def simplecal(num1,num2,cal):
    if cal=='+':
        return num1+num2
    elif cal=='-':
        return num1-num2
    elif cal=='*':
        return num1*num2
    elif cal=='/':
        if num2!=0:
            return num2/num2
        else:
            return 'error division by zero'
    else:
        return 'invalid operation'
res = simplecal(10,20,'*')
print(res)'''
num=20
num2=24
per=(num/num2)*100
print(per)        




             



