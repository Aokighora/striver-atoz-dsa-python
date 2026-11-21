def main():
    pattern20()

def pattern20():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                indices=list(range(1,n+1)) + list(range(n-1,0,-1))
                print("\n".join("*"*i + " "*(2*(n-i)) + "*"*i for i in indices))
                break

        except ValueError:
            pass

main()