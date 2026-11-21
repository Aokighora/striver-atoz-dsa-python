def main():
    pattern21()

def pattern21():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(1,n+1):
                    if i==1 or i==n:
                        print("*"*n)
                    else:
                        print("\n".join(["*"+" "*(n-2)+"*"]))
                break
        except ValueError:
            pass

main()