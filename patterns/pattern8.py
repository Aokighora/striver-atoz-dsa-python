def main():
    print(pattern8())

def pattern8():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                return "\n".join([" "*(n-i) + "*"*(2*i-1) + " "*(n-i) for i in range(n,0,-1)]) 

        except ValueError:
            pass

main()