def main():
    print(pattern9())

def pattern9():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,100):
                u="\n".join([" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i) for i in range(n)]) 
                l="\n".join([" "*(n-i) + "*"*(2*i-1) + " "*(n-i) for i in range(n,0,-1)]) 
                return u + "\n" + l
            
        except ValueError:
            pass

main()
                    