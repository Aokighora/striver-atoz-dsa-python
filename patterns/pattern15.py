def main():
    pattern15()

def pattern15():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(n,0,-1):
                    for j in range(i):
                        print(chr(ord("A")+j),end="")
                    print()
                break

        except ValueError:
            pass

main()