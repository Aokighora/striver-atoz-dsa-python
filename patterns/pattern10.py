def main():
    print(pattern9())

def pattern9():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                u="\n".join(["*"*i for i in range(1,n+1)])
                l="\n".join(["*"*(i+1) for i in range(n-2,-1,-1)])
                return u + "\n" +l

        except ValueError:
            pass

main()