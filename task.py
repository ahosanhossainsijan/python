'''mylist=[1,2,3,4,5]
mylist.pop(2)
print(mylist)'''
'''
l=[]
n=int(input("enter the upper limit"))
for i in range(0,n):
 a=int(input("enter the numbers"))
 l.append(a)
 maxno=l[0]
for i in range(0,len(l)):
 if l[i]>maxno:
  maxno=l[i]

print("The maximum number is ",maxno)
'''
'''
items = [5, 7, 10, 12, 15]
print("list of items is", items)
x = int(input("enter item to search:"))
i = flag = 0
while i < len(items):
 if items[i] == x:
  flag = 1
  break
 i = i + 1
if flag == 1:
 print("item found at position:", i + 1)
else:
 print("item not found")
 
'''
'''
mydict ={"name": "Sijan","age": 22,"email": "sijan@gmail.com"}
for x in mydict:
  print(x)

for x in mydict:
  print(mydict[x])
  '''
dict1 = {'a':10 , 'b': 8}
dict2 = {'c':6 , 'd':4}

 

dict2.update(dict1)

 

print(dict2)
 
