def main():
    pattern17()

def pattern17():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(1,n+1):
                    a=chr(ord("A")+n-i)
                    for j in range(i):
                         print(a,end="")
                         a=chr(ord(a)+1)
                    print()
                break

        except ValueError:
            pass

main()


                        