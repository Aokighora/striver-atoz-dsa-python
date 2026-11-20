def main():
    pattern16()
    pattern166()

def pattern16():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                a="A"
                for i in range(1,n+1):
                    for j in range(i):
                        print(a,end="")
                    a=chr(ord(a)+1)
                    print()
                break

        except ValueError:
            pass

def pattern166():
    while True:
            try:
                n=int(input("No.: "))
                if n in range(1,101):
                    for i in range(1,n+1):
                        print(chr(ord("A")+i-1)*i)
                    break

            except ValueError:
                pass

main()