def main():
    print(pattern4())
    pattern44()


def pattern4():
    while True:
        try:
            n=int(input("Enter a no: "))
            if 1<=n<=100:
                return "\n".join([f"{i}"*i for i in range(1,n+1)])
        except ValueError:
            pass

# using nested for loops

def pattern44():
    while True:
        try:
            n=int(input("no.: "))
            if 1<=n<=100:
                for i in range(1,n+1):
                    for j in range(i):
                        print(i,end="")
                    print()
                break    

        except ValueError:
            pass

main()





      

