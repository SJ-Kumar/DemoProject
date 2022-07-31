f=open(r"C:\Users\jayan\Desktop\Study Plan.txt","r")
c=[]
for x in f:
    print(x)
    c.append(x.split(' '))
    print(c)
    d=0
    for i in range(len(c)):
        d=d+1
        print(len(c))