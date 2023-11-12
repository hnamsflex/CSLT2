n=str(input("Enter the name of a note:"))
x=n[0:1]
y=n[1:2]
z=int(y)
C4= 261.63
D4= 293.66
E4= 329.63 
F4= 349.23 
G4= 392.00 
A4= 440.00 
B4= 493.88
if(x=='C'):
    f=C4/(2**(4-z))
elif(x=='D'):
    f=D4/(2**(4-z))
elif(x=='E'):
    f=E4/(2**(4-z))
elif(x=='F'):
    f=F4/(2**(4-z))
elif(x=='G'):
    f=G4/(2**(4-z))
elif(x=='A'):
    f=A4/(2**(4-z))
elif(x=='B'):
    f=B4/(2**(4-z))
print(f)