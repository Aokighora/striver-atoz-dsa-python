def main():
    pattern19()

def pattern19():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(n,0,-1):
                    a="*"*i
                    s=" "*(2*(n-i))
                    print(a+s+a)
                for j in range(1,n+1):
                    a="*"*j
                    s=" "*(2*(n-j))
                    print(a+s+a)
                break

        except ValueError:
            pass

main()
        