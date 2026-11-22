def main():
    armstrong()

def armstrong():
    n=int(input("No.: "))
    if 0<=n<=10**9:
        dup=n
        if n==0:
            print("True")
        else:
            s=0
            while n>0:
                d=n%10
                s+=(d*d*d)
                n//=10
            if dup==s:
                print("True")
            else:
                print("False")

    else:
        print("Invalid input")
    

if __name__=="__main__":
    main()












if __name__=="__main__":
    main()