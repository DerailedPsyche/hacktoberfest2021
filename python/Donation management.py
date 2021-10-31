#A donation management database program.
#This program enters the name and donation made by them in a database. And later it can search for the donation made by any person in the database.


def Donation(): #creating a function called 'Donation'
    k=1 
    while k==1: #this condition is so that the program never stops and hence can be used again and again.
        
        x=input('enter 0 if you want to find the data and enter 1 if you want to add data')  
        #x telles the program if the user wants to enter data into the database or retrive it.
        
        if x!='1' or '0': #If the user doesn't enter anything other than 0 or 1. The program will just restart
            break
        
        if x=='Password': #this condition allows the technician to stop the machine and retrive all the data if needed.
            k=0
            break
        
        
        
        while x=='1':
            name=input('Enter the name of the Person, Leave Blank if you want to quit') #the name is stored in the variable "name"
            if name=='':
                break #If the user doesnt enter anything, the program will just restart
            money=int(input('Enter the amount donated')) #the amount is stored in the variable "money"
            if money=='':
                break #If the user doesnt enter anything, the program will just restart
            d[name]=money
            
        while x=='0':
            ask_name=input('Enter the Name of the person, Press enter if you want to stop') #the name that has to be searched in the database is stored in the variable 'ask_name'
            if ask_name=='':
                break  #If the user doesnt enter anything, the program will just restart
            elif ask_name in d:
                print(ask_name,' has donated ',d.get(ask_name))
            else: #if the name is not present in the database, this message will be shown
                print('Such name does not exist in the database')
        
    
    
d={}  #Creating a dictonary 'd' in order to store the data
#the dictonary is made outside the database so that it can be retrived later if wanted.

Donation()
x=input('Retrive data YES or NO')
if x=='YES':
    print(d)
else: #if the technician doesn't write YES the program will ask them one more time
    print('Are you sure? All data will be lost')
    x=input('Retrive data YES or NO')
    if x=='YES':
        print(d)
        
print('Have a Nice Day')
