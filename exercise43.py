n=str(input())
x=n[0:1]
y=n[1:4]
z=int(y)
if(z==1):
    print('George Washington')
elif(z==2):
    print('Thomas Jefferson')
elif(z==5):
    print('Abraham Lincoln')
elif(z==10):
    print('Alexander Hamilton')
elif(z==20):
    print('Andrew Jackson')
elif(z==50):
    print('Ulysses S. Grant')
elif(z==100):
    print('Benjamin Franklin')
else:
    print('No such note exists.')