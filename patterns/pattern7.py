def main():
    print(pattern7())

def pattern7():
    while True:
        try:
            n=int(input("Enter a no.: "))
            if n in range(1,101):
                return "\n".join([" "*(n-i)+"*"*(2*i+1)+" "*(n-i) for i in range(n)]) 

        except ValueError:
            pass

main()        