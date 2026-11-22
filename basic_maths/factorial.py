def main():
    factorial()

def factorial():
    n=int(input("No.: "))
    if 0<=n<=10:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)
    else:
        print("Out of range")

if __name__=="__main__":
    main()