def main():
    pattern14()
    pattern144()

def pattern14():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(1,n+1):
                    a="A"
                    for j in range(i):
                        print(a,end="")
                        a=chr(ord(a)+1)
                    print()
                break

        except ValueError:
            pass

#without variable a

def pattern144():
     while True:
            try:
                n=int(input("No.: "))
                if n in range(1,101):
                    for i in range(1,n+1):
                        for j in range(i):
                            print(chr(ord("A")+j),end="")
                        print()
                    break

            except ValueError:
                pass

main()