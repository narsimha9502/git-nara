#write a python function that uses conditional parameters to check if a number is even or odd
def even_odd():
    num=int(input('enter a number:'))
    if num%2==0:
        print('even')
    else:
        print('odd')
even_odd() 
#Describe and provide an example of how to use elif in a python program
num = int(input('enter a number:'))
if num==0:
    print('zero')
elif num>0:
    print('positive number..')
else:
    print('negetive number') 
#write a python script that prints the number from 1 to 10 using a for loop and range function
for i in range(1,10):
    print(i)
#provide a python program demonstrate the use of the break statement inside loop
for i in range(1,10):
    if i==7:
        break
    else:
        print(i)
#Develop a python program calculate students marks grade
marks=int(input('enter a number:'))
if marks>=90:
    print('A grade')
elif marks>=80 and marks<=89:
    print('B grade')
elif marks>=70 and marks<=79:
    print('C grade')
elif marks>=60 and marks<=69:
    print('D grade')
else :
    print('E grade') 
# simple calculator using function
def simple_cal(num1,num2,cal):
    if cal=='add':
        return num1+num2
    elif cal=='sub':
        return num1-num2
    elif cal=='mul':
        return num1*num2
    elif cal=='div':
        if num2!=0:
            return num1/num2
        else:
            return "error"
    else:
        return 'error'
num1=int(input('enter a number:'))
num2=int(input('enter a number:')) 
cal=input('enter a calcution(add,sub,mul,div)')   
res = simple_cal(num1,num2,cal)   
print(res)
#using range function to generate and print even numbers b/w 1 to 50
for i in range (1,50):
    if i%2==0:
        print(i)     
               

        