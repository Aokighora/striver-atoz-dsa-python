def  main():
    pattern12()

def pattern12():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                for i in range(1,n+1):
                    l="".join([str(j) for j in range(1,i+1)])
                    s=" "*(2*(n-i))
                    r="".join([str(j) for j in range(i,0,-1)])
                    print(l+s+r)
                break

        except ValueError:
            pass

main()