x = input("Enter character: ")
y = int(input("Enter no.of rows: "))

for i in range(1,y+1):
    if i == 1:
        print(x.center(y*2-1,' '))
    elif i == y:
        print(x*(i*2-1))
    else:  
        j = " "*(i*2-3)
        k = j.center(len(j)+2,x)
        print(k.center(y*2-1,' '))

