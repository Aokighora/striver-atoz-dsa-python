def main():
    print(pattern3())

def pattern3():
    while True:
        try:
            n=int(input("Enter the level: "))
            rows=[] 
            if 1<=n<=100:
                for i in range(1,n+1):
                    row=""
                    for j in range(1,i+1):      
                                                 # concatenation, not list insertion
                        row+=str(j)
                    rows.append(row)
                return "\n".join(rows)
            
        except ValueError:
            pass
main()