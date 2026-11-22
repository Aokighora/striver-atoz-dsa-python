def main():
    max_digit()

def max_digit():
    n=int(input("No.: "))
    if 0 <= n <= 5000:
        maxi=0
        while n>0:
            ld=n%10
            if ld>maxi:
                maxi=ld
            n//=10
        print(maxi)
            
    else:
        print("out of range")

if __name__=="__main__":
    main()