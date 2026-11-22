def main():
    reverse()

def reverse():
    n=int(input("No.: "))
    if 0 <= n <= 5000:
        rev=0
        while n>0:
            ld=n%10
            rev=rev*10 + ld
            n//=10
        print(rev)
    else:
        print("out of range")

if __name__=="__main__":
    main()