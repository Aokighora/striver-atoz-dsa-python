def main():
    pattern5()
    print(pattern55())

# using for loop 

def pattern5():
    while True:
        try:
            n=int(input("Enter a no.: "))
            if n in range(1,101):
                for i in range(n,0,-1):
                    print("*"*i)
                break

        except ValueError:
            pass

def pattern55():
    while True:
        try:
            n=int(input("No.: "))
            if n in range(1,101):
                return "\n".join(["*"*i for i in range(n,0,-1)])
            break
            
        except ValueError:
            pass

main()        












          