a = int(input('enter the number'))
i = 1
while i<a+1:
    if i % 5 ==0:
        if i % 2 ==0:
            continue
        print(i, end =' ')
