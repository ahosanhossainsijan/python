'''x=5
y=9
print('result is :',x+y)
a=int( input('ENTER A NUMBER :'))
print(x+a)
for z in range (a,0,-2):
    print(z)
    if z>3 and z<5:
        print('I LOVE MYSELF')
    elif z>2 or z<6:
        print('I LOVE MY FAMILY')
    else :
        print('I LOVE YOU')
while z<15:
    print(z)
    print('DO I LOVE YOU??')
    z=z+1
print('Finish')

print('HELLO\t I LOVE \"YOU\" \\ \nDO YOU LOVE ME?')

n='Nishu'
print(n[0])
print(len(n))
print(n[4])

print(str.lower(n))
print(str.upper(n))
for c in n:
    print(c)
print(ord(n[0]))
print(chr(83))
'''
text = open("sijan.txt").read()
print (text)
count=0
for line in open("sijan.txt").read():
    print(line)
    count+=1
print(count)









