def main():

    #keep taking user input until correct
    # n must be 1<=n<=1000
    #print a sequence of 1 at the top to n stars at the bottom
    print(pattern2())

def pattern2():
    while True:
        try:
            n=int(input("Enter the level: "))
            if 1<=n<=100:
                return "\n".join(["*"*i for i in range(1,n+1)])

        except ValueError:
            pass    
main()






