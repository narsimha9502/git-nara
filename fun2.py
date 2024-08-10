"""class car():
            def __init__(self):
            self.brand="AUDI"
            self.cc=4200
            self.color="red"
        def engine_start(self):
            print("engine is starting..")
        def start_gear(self):
            print("shifting gear")
        def acceleration(self):
            print("car is acceleration")
        c1=car()
        print(c1.brand)
        print(c1.cc)
        print(c1.color)
        c1.engine_start()
        c1.start_gear()"""
"""class football:
    def __init__(self,name,team,goals):
     self.name=name
     self.team=team
     self.goals=goals 
    def shooting(self):
       print(self.name,"is shotting")
    def passing(self):
       print(self.name,"passing")
    def running(self):
       print(self.name,"is running") 
    def display(self):
       print(self.name)
       print(self.team)
       print(self.goals) 
       self.shooting()
       self.passing()
       self.running()              
cr=football("cristiano","juventu",730)
cr.display()
messi=football("Messi","baracelona",700)
messi.display()"""
"""class loan:
    def farmer_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        r=10
        si=(p*t*r)/100
        print("simple interest",si)
    def car_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        r=10
        si=(p*t*r)/100
        print("simple interest",si)    
farmer=loan()
farmer.farmer_loan()
farmer.car_loan()"""
"""class loan:
    r=10
    def farmer_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        si=(p*t*loan.r)/100
        print("simple interest",si)
    def car_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        si=(p*t*loan.r)/100
        print("simple interest",si)    
farmer=loan()
farmer.farmer_loan()
farmer.car_loan()"""
'''class loan:
    def farmer_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        global r
        r=10
        si=(p*t*r)/100
        print("simple interest",si)
    def car_loan(self):
        p=float(input("enter amount:"))
        t=float(input("enter time:"))
        si=(p*t*r)/100
        print("simple interest",si)    
farmer=loan()
farmer.farmer_loan()
farmer.car_loan()'''
#write a for loop to print numbers from 1 to 10
'''for i in range(1,11,1):
    print(i)'''
#write a for loop to iterate through a list of fruits 
'''fruit=['apple','banana','cherry','date']
for f in fruit:
    print(f)'''    
#write a for loop to calculate and print the factorial of a given number
'''num=7
factorial=1
for i in range(1,num+1):
    factorial*=i
    print(f'the factorial of {num} is {factorial}')'''
#write a for loop to print the multiplication table 5
'''num=5
for i in range(1,11):
    mul=num*i
    print(f'{num} x {i} = {mul}',)'''
'''number=19
for z in range(1,11):
    table=number*z
    print(f'{number} x {z} = {table}')'''
'''student_grades={'Alice':85,'Bob':78,'Charlie':92}
for i in student_grades.items():
    print(i) '''
'''total = 0
for number in range(1,101):
    if number%2==0:
        total=total+number
        print(f'the sum of all even number is 1 to 100 is: {total}')'''
'''class quizapp:
    q=('what is the cap of india','what is the cap of karnataka','what is the capital of maharastra')
    ans=('delhi','bangalore','mumbai')
    for x in q:
        print(x)
        user=input('enter ans').lower()
        if user in ans:
            print('correct ans')
        else:
            print('wrong ans')'''
#mutliplication
num=int(input('enter a number'))
for i in range(1,num+1,1):

            





                