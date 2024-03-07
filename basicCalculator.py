def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2;
def pro(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2;

print('\nSelect the operation to perform:\n1.Add\n2.Subtract\n3.Multiplication\n4.Divide\t')
ch= int(input());
n1=int(input('\nFirst number:\t'))
n2=int(input('Second number:\t'))

if(ch==1):
    print(add(n1,n2))
if(ch==2):
    print(sub(n1,n2))
if(ch==3):
    print(pro(n1,n2))
if(ch==4):
    print(div(n1,n2))