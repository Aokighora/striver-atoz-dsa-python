def main():
    pattern11()

def pattern11():
    while True:
        try:
            n=int(input("No.: "))
            rows=[]
            if n in range(1,101):
                for i in range(n):
                    for j in range(i+1):
                        if (i+j)%2==0:
                            print("1",end="")
                        else:
                            print("0",end="")
                    print()
                break
                    
        except ValueError:
            pass

main()
