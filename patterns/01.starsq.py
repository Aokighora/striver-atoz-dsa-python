def main():
    # print a square of dim(n)
    # n must be 1<=n<=1000
    # should keep taking input from user until correct
    print(square())

def square():
    while True:
        try:
            n=int(input("Enter the size of square: "))
            if 1<=n<=1000:
                return "\n".join(["*"*n for _ in range(n)])
        except ValueError:
            pass

main()             

        