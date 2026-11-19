def main():
    print(pattern6())

def pattern6():
    while True:
        try:
            n=int(input("No.: "))
            rows=[]
            if n in range(1,101):
                for i in range(n,0,-1):
                    row=""
                    for j in range(1,i+1):
                        row+=str(j)
                    rows.append(row)
                return "\n".join(rows)

        except ValueError:
            pass

main()
                        