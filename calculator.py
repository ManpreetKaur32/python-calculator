# print('''
# + ADD
# - SUBTRACT
# * MULTIPLY
# /DIVISION''')

# num1 = int(input("enter number 1 : "))
# num2 = int(input("enter number 2 : "))
# oper = input("enter operator(+,-,*,/) : ")

# if oper == "+":
#     print(num1+num2)
# elif oper=="-":
#     print(num1-num2)
# elif oper == "*":
#     print(num1*num2)
# elif oper=="/":
#     print(num1/num2)
# else:
#     print("invalid operatore")



# if oper == "+":
#     print(num1+num2)
# if oper=="-":
#     print(num1-num2)
# if oper == "*":
#     print(num1*num2)
# if oper=="/":
#     print(num1/num2)
# else:
#     print("invalid operatore")

#output : 7
#invalid operatore
#this happen, because else work for "/" operation, not for others, thats why in running time, the condition check correspond to "/" operator differently and its output show differntly. that's why we show these two operator.



#the aboe problem could sourt out as below :
# if oper == "+":
#     print(num1+num2)
# if oper=="-":
#     print(num1-num2)
# if oper == "*":
#     print(num1*num2)
# if oper=="/":
#     print(num1/num2)
# if oper!="+" and oper!="-" and oper!="*" and oper!="/":
#     print("invalid operatore.......")


# for loop

# for n in range(1,11):
#     print("2","*",n,"=",2*n)

#output : 
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20



#rang in reverse order
# for n in range(10,0,-1):
#     print("2","*",n,"=",2*n)

#output :
# 2 * 10 = 20
# 2 * 9 = 18
# 2 * 8 = 16
# 2 * 7 = 14
# 2 * 6 = 12
# 2 * 5 = 10
# 2 * 4 = 8
# 2 * 3 = 6
# 2 * 2 = 4
# 2 * 1 = 2 

w="Welcome to india"
# print(w[-1::-2 ])

#output : w


#string iteration
# l=len(w)
# print(l)
# for a in range(l):
#     # print(a)
#     print(w[a])


#now we have to print in resverse order

#first method

# w1=w[-1::-1]
# l=len(w1)
# print(l)
# for a in range(l):
#     # print(a)

#     print(w1[a])


#second method

# l=len(w)
# print(l)
# for a in range(l-1,-1,-1):
#     # print(a)
#     print(w[a])



#chr() and ord()

# a = 67;
# print(chr(a))


# l = "M";
# print(ord(l))


# w=["welcometoindia"]
# L=[10,20,30,45,10,50,20]
# # m=L.index(20)
# # print(m)
# c=L.count(20)
# print(c)



#zip()

# l=[10,20,30,40]
# l1=[11,2,33,4]

# for a,b in zip(l, l1):
#     print(a)
#     print(b)



# l=[]
# for a in range(1,4):
#     a1=input("enter value" + str(a) + ": ")
#     l.append(a1.split())
# print(l)


#stack and queue

l=[]
while True:
    c=int(input('''
    1 Push Element
    2 Pop Element
    3 Peek Element
    4 Display Element
    5 Exit
    '''))

    if c==1:
        d=input("Enter Value : ")
        l.append(d)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Stack is empty")
        else:
            print("The last element removed : ", l.pop())
            print(l)
    elif c==3:
        if len(l)==0:
            print("Stack is empty")
        else:
            print("The last element is : ", l[-1])
            print(l)
    elif c==4:
        print("The stack elements are : ", l)

    elif c==5:
        break

    else:
        print("invalid operation...............")




