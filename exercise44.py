m=str(input())
d=int(input())
if((m=='January') and (d==1)):
    print('New year’s day')
elif((m=='July') and (d==1)):
    print('Canada day')
elif((m=='December') and (d==25)):
    print('Christmas day')
else:
    print(m,d)