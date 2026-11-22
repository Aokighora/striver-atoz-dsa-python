def main():
    palindrome()

def palindrome():
    n=int(input("No.: "))
    if 0 <= n <= 5000:
        dup=n
        rev=0
        while n>0:
            ld=n%10
            rev=rev*10 + ld
            n//=10
        if rev==dup:
            print("True")
        else:
            print("False")

    else:
        print("out of range")

if __name__=="__main__":
    main()