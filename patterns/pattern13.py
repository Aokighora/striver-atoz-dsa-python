def main():
    pattern13()

def pattern13():
    while True:
        try:
            n=int(input("Enter a no.: "))
            if n in range(1,101):
                num=1
                for i in range(1,n+1):
                    for j in range(i):
                        print(num,end="")
                        num+=1
                    print()
                break

        except ValueError:
            pass

main()
