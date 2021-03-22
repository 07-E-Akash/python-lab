n=int(input('enter the number'))
sum=0
temp=n
while temp>0:
            rem=temp%10
            sum=sum+rem**3
            temp//=10
if n==sum:
    print('number is armstrong')
else:
    print('number is not armstrong')

