
def countdown(x):
    if x==0:
        print("Blastoff!")#Base case
    else:
        print(x)
        countdown(x-1)#Recursive case
countdown(4)

#Factorial is an example of recusion
#Viruses and scientific programs use recursion
#Base statement is used for termination
#Else statement checks the negative condition
