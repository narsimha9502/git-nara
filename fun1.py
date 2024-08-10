"""class facebook:
    def __init__(self):
        self.username=input("enter username:")
        self.phone=983191
        self.email="facebook@gmail.com"
f1=facebook()
print(f1.username)
print(f1.phone)
print(f1.email)  """

'''class car:
    def __init__(self):
        self.brand="BMW"
        self.cc=2100
        self.color="blue"

def start_engine(self):
    print("Engine is starting")
def start_gear(self):
    print("shifting gear")
def accelerate(self):
    print("car is accelerating")

c1=car()
print(c1.brand)
print(c1.cc)'
print(c1.color)

c1.start_engine()
c1.start_gear()
c1.accelerate() '''
'''tv=int(input('enter no.of tvs manufactured:'))
work_hours=int(input('enter no.of working hours:'))
if tv>=5 and work_hours>=9:
    print('salary','Rs',tv*100)
else:
    print('salary','Rs',tv*50) '''
''''value1=float(input('enter price of first product:'))
value2=float(input('enter price of second product:')) 
total_amount=value1+value2
if value1>=1000 and value2>=1000:
    print('total_amount:',total_amount) 
    print('discount 25%:',total_amount*25/100)                   
else:
    print('total_amount:',total_amount)
    print('no discunt:')'''
'''name=input('enter name:')
age=int(input(f'{name} enter age:'))
if age>=18 and age<30:
    print(f'{name} has to pay 4$')
elif age>=30 and age<60:
    print(f'{name} has to pay 6$')
elif age>=60:
    print(f'{name} free ticket')
else:
    print(f'{name} not allowed')  '''
'''name=input('enter name:')
percentage=int(input(f'{name} enter percentage:'))
if percentage>=35 and percentage<50:
    print(f'{name} grade is c')
elif percentage>=50 and percentage<80:
    print(f'{name} grade is B')
elif percentage>=80 and percentage<=100:
    print(f'{name} grade is A')  
elif percentage>100:
    print(f'{name} is invalid')
else:
    print(f'{name} got fail..') '''
'''var = 'rajkanth'
print(var[::-1]) '''
'''def pallindrome():
    val='mom'
    if val[::1]==val[::-1]:
        print('pallidrome')
    else:
        print('not pallindrome')  
pallindrome() '''
'''letter = 'i am a student'
for i in letter:
    print(''.join(format(ord(i),'b'))) '''
'''print('\U0001f600') 
print('\U0001f601')
print('\U0001f602')'''
'''value = 'raj'
print(value.upper())
value = 'RAJ'
print(value.lower())
value = 'raj'
print(value.swapcase())
value = 'raj'
print(value.title())'''
'''val='raj'
for x in val:
    v=ord(x)
    conv=v-32
    print(chr(conv),end='')'''
'''value='RAJ'
for x in value:
    v=ord(x)
    conv=v+32
    print(chr(conv),end='') '''
'''val='AAJ RRR'
v=val.split()
for x in v:
    p=x.lower()
    print(p)
    for y in range(len(p)):
        if y==0 :
            print(y.upper(),end='')
        elif y>0:    
            print(y.lower(),end='')'''
'''c_ans=0
w_ans=0
print('1.what is the capital city of india')
user=input('enter answer:').lower()
if user=='delhi':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('2.what is the capital city of karnataka')
user=input('enter answer:').lower()
if user=='bangalore':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=c_ans+1 
print('3.what is the capital city of kerala')
user=input('enter answer:').lower()
if user=='thiruvanthapuram':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('4.what is the capital city of madhya pradesh')
user=input('enter answer:').lower()
if user=='bhopal':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('5.what is the capital city of maharastra')
user=input('enter answer:').lower()
if user=='mumbai':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('6.what is the capital city of assam')
user=input('enter answer:').lower()
if user=='dispur':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('7.what is the capital city of bihar')
user=input('enter answer:').lower()
if user=='patna':
    print('correct')
    c_ans=w_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('8.what is the capital city of goa')
user=input('enter answer:').lower()
if user=='panaji':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1'''
'''print('9.what is the capital city of gujarath')
user=input('enter answer:').lower()
if user=='gandhinagar':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    w_ans=w_ans+1
print('10.what is the capital city of chhattisgarh')
user=input('enter answer:').lower()
if user=='raipur':
    print('correct')
    c_ans=c_ans+1
else:
    print('wrong')
    c_ans=c_ans+1

neg_marks=(w_ans)*.25
total=c_ans-neg_marks    
per=(total/(c_ans+w_ans))*100
print('percentage',per)'''

'''val ='rama'
print(val.isnumeric())
val1 = '123'
print(val1.isnumeric())
val12 = 'rama'
print(val1.isalnum())
val123 = '123'
print(val1.isalnum())'''
'''password = input('Enter password')
alpha_count=0
numeric_count=0
spl=0
if len(password)>=8 and len(password)<=13:
    for x in password:
        if x.isalpha():
            alpha_count=alpha_count+1
        elif x.isnumeric():
            numeric_count=numeric_count+1
        else:
            spl=spl+1
if alpha_count>=4 and numeric_count>=4 and spl>=1:
    print('valid password')
else:
    print('invalid') '''
'''a=[10,20,30]
print(a[1])'''
'''b=[10,20,30,[50,60]] 
print(b[3][1]) '''
'''a=[1,2,3,4,[3,4,3,6],70]
print(a[5]) 
b=[3,4,3,6,1,[60,70,80,90,[30,601]]]
print(b[-1][-1][-1])'''
'''c= [100,200,300,400,[11,12,13],[60,70]]
print(c[-1][-1])'''
'''a=[1,2,3,6,101,5,10,9]
print(a.sort(),a)'''
'''a=100
b=20
if a>b:
    a,b=b,a
    print('a=',a)
    print('b=',b)
else:
    a,b=b,a    '''
'''a=[10,20,30,6,101,5,1,10,9]
for x in range(len(a)):
    for y in  range(len(a)):
        print(a[x],a[y])'''
'''a=[10,20,30,6,101,5,1,10,9]
for x in range(len(a)):
    for y in  range(len(a)):
        if a[x]>a[y]:
                a[x],a[y]=a[y],a[x]
        else:
            a[x],a[y]=a[x],a[y]    
print(a) ''' 
'''a=[10,20,30,6,101,5,10,9,1004]
a.sort()
print(a[0]+a[-1])'''
'''a=[10,20,30,6,101,5,10,9,1004]
b=len(a)
v=b//2
print(a[v])'''
'''a=[10,20,30,6,101,5,10,9,1004]
print(a[len(a)//2])'''
''''a=[10,20,30]
a.append(40)
print(a)'''
'''a=[10,20,30]
a.insert(2,100)
print(a)'''
'''a=[110,20,30]
b=[11,12]
a.extend(b)
print(a)'''
'''a=[10,2,3,5,7,10,3]
a.remove()
print(a)'''
'''a=[10,2,3,5,7,10,3]
b=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        pass
print(b) '''
'''a=[10,2,3,5,7,10,3]
b=[]
[b.append(x) for x in a if x not in b]
print(b)'''
'''a=[10,2,3,5,7,10,3]
b=[]
[b.append(x) for x in a if x not in b]
print(b) '''
'''a=[10,2,3,5,7,10,3]
b=[]
x=[x for x in a if x%2==0] 
print(x)'''
'''sales=()
print(type(sales))'''
'''a={'rama','ravi','arjun'}
b={'rama'}
c=a.intersection(b)
print(c)
a={'rama','ravi','arjun'}
b={'rama'}
c=a.difference(b)
print(c)
a={'rama','ravi','arjun'}
b={'rama'}
c=a.symmetric_difference(b)
print(c)
a={'rama','ravi','arjun'}
b={'rama'}
c=a.union(b)
print(c)'''
# 1
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=python.intersection(sql)
print(c)
#2
python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=python.symmetric_difference(sql)
print(c)
#3
python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=python.intersection()
print(c)
#4
python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=python.union(sql)
print(c)
#4
python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=python.symmetric_difference(sql)
print(c)'''
###########
# 1
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
java={'surabhi','bhumi','yashwanth','babu','danish','raj'}
c=(python&sql-java)|(python&java-sql)|(java&sql-python).union()
print(c)'''
#2
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
java={'surabhi','bhumi','yashwanth','babu','danish','raj'}
c=python-sql-java.union()|java-python-sql.union()|java-sql-python.union()
print(c)'''
#4
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
c=len(python.union(sql))
d=python.union(sql)
print(c) 
print(d)'''
#5
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
java={'surabhi','bhumi','yashwanth','babu','danish','raj'}
c=python.union(sql).union(java)
s=c-java
print(s)'''

#6
'''python={'surabhi','bhumi','yashwanth','babu','danish'}
sql={'surabhi','bhumi','yashwanth','manish','ramesh'}
java={'surabhi','bhumi','yashwanth','babu','danish','raj'}
c=python|sql|java
d=len(c)
print(c)
print(d)'''

'''class Alpha:
    def fun(self):
        print('Alpha class fun()')
class Beta(Alpha):
    pass
b=Beta()
b.fun()'''

'''class customer:
    def sel_restarent(self):
        print('restarent selected')
    def sel_items(self):
        print('items selected')
class platinum_customer(customer):
    pass
r=platinum_customer()
r.sel_restarent()
r.sel_items() '''
'''class Alpha:
    def fun1(self):
        print('inside alpha fun1()')
class Beta(Alpha):
    def fun2(self):
        print('inside beta fun2()')
class Gamma(Beta):
    pass
g=Gamma()
g.fun1()
g.fun2()'''
#multi level inheritance
'''class plane:
    def fly(self):
        print('flying')
    def landing(self):
        print('landing')
class cargo_plane(plane):
    def carry_goods(self):
        print('carring goods')  
c=cargo_plane()
c.carry_goods()
c.fly()
c.landing()        
class passanger_plane(plane):
    def carry_passengers(self):
        print('carring passengers')   
p=passanger_plane()
p.carry_passengers()
p.fly()
p.landing()        
class fighter_jet(plane):
    def carry_weapons(self):
        print('carring weapons')
f=fighter_jet()                    
f.carry_weapons()
f.fly()
f.landing()
class '''
'''class alpha:
    def fun1(self):
        print('alpha class fun1()')
class beta:
    def fun2(self):
        print('beta class fun2()')
class gamma(alpha,beta):
    pass
g=gamma()
g.fun1()
g.fun2() '''

'''class messenger:
    def send_message(self):
        print('text message is sent')
    def receive_message(self):
        print('text message is receive')
class internalMessage(messenger):
    pass
class whatsappMessanger(messenger):
    def send_message(self):
        print('text,photos,videos and file sent')
    def receive_message(self):
        print('text,photos,videos and file is recived')
    def set_up(self):
        print('DP is set')
    def set_status(self):
        print('status is set')
lm=internalMessage()
lm.send_message()
lm.receive_message()'''
'''try:
    a=int(input('enter a number: '))  
    b=int(input('enter a number: '))
    c=a/b
    print(c)
except ZeroDivisionError:
    print('denominator nerver be zero') 
except ValueError:
    print('strings are not allowed')                         
except IndentationError:
    print('improper identation') 
except NameError:
    print('name error') '''
'''try:
    marks=int(input('enetr marks: '))
    if marks<0 or marks>100:
        raise Exception('marks are invalid')
    else:
        print(marks)
except Exception as e:
    print(e)  '''
'''lower=100
upper=2000
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
        r=temp%10
        sum=sum+r**order
        temp//10
    if sum==num:
        print(num) '''
'''n=2
i=0
while i<10:
    if n%2==0 and n%7==0:
        print(n)
        i+=1
    n+=2 '''
'''listOfStrings=['tic','toc','toe']
for i in listOfStrings:
    for j in i:
        if j !='t':
           print(j) '''
'''listOfElements=['a','b','c','d','k','h','i']
for i in listOfElements:
    if i=='k':
      break
    print(i)'''
import tkinter as tk
from tkinter import messagebox

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Grocery App")

        # Initialize grocery items (you can extend this list)
        self.grocery_items = [
            {"name": "Apples", "price": 1.99},
            {"name": "Bananas", "price": 0.99},
            {"name": "Bread", "price": 2.49},
            {"name": "Milk", "price": 1.79},
            {"name": "Eggs", "price": 2.29}
        ]

        # Initialize selected items list
        self.selected_items = []

        # Create UI elements
        self.create_ui()

    def create_ui(self):
        # Create a frame to hold the grocery items list
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Create checkboxes for each grocery item
        self.checkboxes = []
        for item in self.grocery_items:
            var = tk.IntVar()
            chk = tk.Checkbutton(frame, text=f"{item['name']} - ${item['price']:.2f}", variable=var, onvalue=1, offvalue=0)
            chk.var = var  # Keep a reference to the IntVar
            chk.pack(anchor=tk.W)
            self.checkboxes.append(chk)

        # Add button to add selected items to cart
        add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack(pady=10)

    def add_to_cart(self):
        # Clear selected items list
        self.selected_items.clear()

        # Iterate through checkboxes to find selected items
        for idx, chk in enumerate(self.checkboxes):
            if chk.var.get() == 1:
                self.selected_items.append(self.grocery_items[idx])

        # Show selected items in a message box (for demo purposes)
        if self.selected_items:
            selected_items_str = "\n".join([item['name'] for item in self.selected_items])
            messagebox.showinfo("Selected Items", f"Items added to cart:\n{selected_items_str}")
        else:
            messagebox.showinfo("No Items Selected", "Please select items to add to cart.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()

                           

    








