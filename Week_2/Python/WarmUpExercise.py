def identitym(n):
    for i in range(n):
        for j in range(n):
            if (i==j)==1:
                print("1",sep="",end="")
            else:
                j=0
                print("0",sep="",end="")
        print()
    return n
n=int(input("Enter size of identity matrix:"))
k=identitym(n)
