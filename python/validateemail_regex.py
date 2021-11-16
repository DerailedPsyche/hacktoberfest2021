# Validate email using Python
  
# import re module for regex
import re 
  
# Regex expression for validating email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   
# Define a function to validate Email 
def check(input):
    # search input to check for email
    if(re.search(regex,email)):  
        print("Valid Email")
    else:  
        print("Invalid Email")  


email = input("Enter email: ")
check(email) 