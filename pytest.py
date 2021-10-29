def main():
    
    n=int(input())
    Virus=list(input())
    flag=0
    for i in range (n):
        newV=Virus.copy()
        b=list(input())
        for j in range(len(b)):
            if(b[j]!=newV[j] and (b[j] not in newV and j>=newV.index(b[j]))or(b[j]in newV and j<=newV.index(b[j]))):
                flag=1
                break
            else:
                flag=0
            
        if flag == 1:
            print("NEGATIVE") 
        else:
            print("POSITIVE")  
        

main()