rows=int(input())
cols=int(input())
lines=["_","/","\\"," "]
if cols%2==1:
    evecir=(cols+1)//2
else:
    evecir=cols//2
for i in range((rows*2)):
    if i==0:
        for j in range(evecir):
            print(lines[3]+lines[0]+lines[3],end="")
            print(lines[3],end="")
        print()
    if i%2==0:
        for j in range(evecir):
            print(lines[1]+lines[3]+lines[2],end="")
            if(j!=evecir-1):
                print(lines[0],end="")
        print()
    else:
        for j in range(evecir):
            print(lines[2]+lines[0]+lines[1],end="")
            print(lines[3],end="")
        print()        
