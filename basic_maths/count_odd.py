def main():
    count_odd()

def count_odd():
    n=int(input("No.: "))
    if 0<=n<=5000:
            c=0
            while n>0:
                ld=n%10
                if ld%2!=0:
                    c+=1
                n//=10
            print(c)
    else:
         print("out of range")
           
if __name__=="__main__":
    main()
