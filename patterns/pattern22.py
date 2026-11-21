def main():
    pattern22()

def pattern22():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(2*n-1):
                    for j in range(2*n-1):
                        top=i
                        bottom=2*n-2-i
                        left=j
                        right=2*n-2-j
                        print(n-min(top,bottom,left,right),end="")
                    print()
                break
        except ValueError:
            pass

main()
