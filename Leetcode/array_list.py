'''#programsto tack user input
#first 
name=input("enter your name")
topic=input("enter your topic")
if(topic=="" or name==""):
    print("please enter a valid topic / name")
else:
    print ("Hi ",name," you selected a topic ", topic ,"it is a very good " ,topic ,"relavent in present world")
# second
books=int(input("enter how many books"))
print("you buy ",books,"of cost $2 each so total amount in INR is",books*2*80)'''
'''#program to chack weather input is palendrome
name=input("enter name").upper() # O(n)
new=(name[::-1]) # O(n)
print(new==name) # O(n)'''
'''# program of ATM
print("A: check balance \n B: withdrawalc\n C: Deposit \n D:mani statement \n E:Exoit")
mani_statement=[]

user_input=input("enter option : ")

balance=10000
while (True):
    match user_input:
        case "A":
            print("you have balance of ",balance)
            
        case "B":
            withdrawal=int(input("how much you want to withdraw?"))
            if withdrawal<100:
                print("please enter withdrawal amount graterthan 100")
            elif(withdrawal>balance):
                print("you don't have sufficient balance for withdraw")
            else:
                print("here you go, your current Balance")
                balance-=withdrawal
                mani_statement.append(withdrawal)
                print(balance)
                
        case "C":
                Depodit=int(input("enter your  deposit ammount"))
                balance+=Depodit
                mani_statement.append(Depodit)
                print("your new balance is ",balance)
                mani_statement.append(balance)
                
        case "D":
                print(mani_statement)
                
        case "E":
            break
        case _:
            print("invalid option please try again")
    user_input=input("A: check balance \n B: withdrawalc\n C: Deposit \n D:mani statement\n E:exit")
    user_input=user_input.upper()    
    if(user_input!="E"):
        True                    
'''
'''Email=input("enter your mail")
# new= Email.split("@")
if Email[-4:]==".com":
    print(Email)
    print("valid email id")
else:
    print("Invalid")'''

# n2=[1,2,3,4,5]
# n1=[3,4,3]    
# n=[]   
# stack=n1
# top=len(n1)-1
# while top>0:
#     for i in range(0,len(n2)):
#         if stack[top]< n2[i]:
#             n.append(n2[i])
#         else:
#             n.append(-1)
# top-=1
# print(n)

'''#stack
l=[3,4,2,1,3,5]
main=[3,2,3]
stack=[]
top=0
for i in range(0,len(l)):
    if l[i]>main[top]:
        stack.append(l[i])
    top+=1
print(stack)'''
'''#alternative merge
a=input("enter your first string")
b=input("enter your second string")
d=min(len(a),len(b))
str=""
for i in range (0,d):
  str+=a[i]+b[i]
if len(a)>len(b):
  str+=a[d::]
else:
  str+=b[d::]
print(str)'''
'''# reversing every string reverse in a line
str1="this is mahee."
if "." in str1:
    print("present")
    str2=str1[:len(str1)-1]
    str2=str2[::-1]
    str2+='.'
    print(str2)
    str2=str1[len(str1)-1]
    str3=str2.split()
    print(str3)'''
'''#continuous sub array which is equal to target
#[3,0,1,4] target =4 ans=[3,0,1]
l=[3,0,4,9]
t=int(input("enter target element"))
for i in range(0,len(l)):
    if t<l[i]:
        break
    elif t==l[i]:
        print(0,i)
    else:'''
'''#Email verification 
email=input('Enter email')
if "@" in email and ".com" in email and email.index('.com')==len(email)-4:
    print("valid email")
else:
    print("invalid email")'''
'''#to verify creadencials
pair = {}

def sigin():
    user=input("Enter user name")
    password=input("enter your password")
    verify=input("enter your passeord again")
    if password==verify:
        pair [user]= password
    else:
        print("your password does not match")
    print(pair)   

def login():
    user=input("Enter username : ")
    password=input("enter your password: ")
    for i in pair: 
        if((user, password) in pair.items()):
            print("hello you are in")
        else:
            print("wrong credentials please try again")
while (True):
    print("A: Sigin \n B:Login")
    choose=input("enter your choise").upper()
    match choose: 
        case "A":
            sigin()
        case "B":
            login()
        case "C":
            break'''
'''#counting number of words in paragraph
paragraph=input("Enter a paragraph")
count=0
for word in paragraph.split():
    count+=1
print("Number of words",count)'''
'''#count for voils and cansonents
sentence=input("Enter a sentence")
vcount=0
ccount=0
for i in (0,len(sentence)):
    if sentence[i]=="aeiou":
        vcount+=1
    else:
        ccount+=1
print(vcount,ccount)'''
'''#printing tabuls
user=int(input("enter the number of tables"))
for i in range (1,user+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)'''

