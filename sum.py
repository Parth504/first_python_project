def read_list():
    l1=[]
    print("Enter list elements until done is pressed")
    while True:
        items=input()
        if items=='done':
            break
        l1.append(int(items))
    return(l1)
num1=0
num2=0
num3=0
l2=[]
l3=[]
list1=read_list()
list2=read_list()
l2=list1[-1::-1]
l3=list2[-1::-1]
for i in l2:
    num1=num1*10+i
for i in l3:
    num2=num2*10+i
#print(num1)23
#print(num2)
num=str(num1+num2)
list3=[]
for i in range(len(num)):
    list3.append(int(num[i]))
print(list3)