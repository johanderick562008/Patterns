import sys

def error():
    print("Inavlid Character")
    sys.exit(0)

def oneside(a,b,c,d):
    r = range(a,b,c)
    for i in r:
        if i == 1: print(x.center(y*2-1,' '))   
        else:
            if d==0 and z%2!=0 and i==y: pass
            else:
                j = " "*(i*2-3)
                k = j.center(len(j)+2,x)
                print(k.center(y*2-1,' '))
             

x = input("Enter character: ")
try:
    y = int(input("Enter no.of rows (graeter than 4): "))
except ValueError: error()
if y<5: error()
z = y
if y%2==0: y =  y//2
else:y = y//2+1
             

oneside(1,y+1,1,1)
oneside(y,0,-1,0)

