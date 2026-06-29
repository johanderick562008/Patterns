x = input("Enter character: ")
y = int(input("Enter no.of rows: "))

for i in range(1,y+1):
    j = x*(i*2-1)
    print(j.center(y*2-1,' '))
