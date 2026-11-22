def main():
    count()

def count():
    while True:
        n=int(input("No.: "))
        if 0<=n<=5000:
            if n==0:
                print(1)
            else:
                c=0
                while n>0:
                    c+=1
                    n//=10
                print(c)
        else:
            print("Out of range")

        break

if __name__=="__main__":
    main()