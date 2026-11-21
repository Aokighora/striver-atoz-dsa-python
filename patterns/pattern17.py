def  main():
    pattern17()

def pattern17():
    while True:
       try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(n):
                    a="A"
                    s=" "*(n-(i+1))
                    print(s,end="")
                    for j in range(2*i+1):
                        print(a,end="")
                        if j<i:
                            a=chr(ord(a)+1)
                        else:
                            a=chr(ord(a)-1)
                    print(s,end="")
                    print()
                break

       except ValueError:
           pass
           

main()