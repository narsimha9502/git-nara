#create a function with variable length of arguments
'''def fun(*a):
    print(a)
fun(10,20,30,40)
fun(90,80,70,60)'''
#return multiple value from function
'''def cal(a,b):
    add=a+b
    sub=a-b
    return add,sub
res=cal(20,40)
print(res)'''
# create a function with default value
'''def emp(name,salary):
    print("name:",name,"salary:",salary)

emp("narasimha",20000) 
emp("raj",19000)'''
# create a inner function to calculate addition
# random otp
import secrets
secretsgenerator=secrets.SystemRandom()
otp=secretsgenerator.randrange(100000,999999) 
print("secure random otp is",otp)   