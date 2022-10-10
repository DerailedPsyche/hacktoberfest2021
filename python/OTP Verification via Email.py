import math
import random
import smtplib


# your email credentials
# Make sure to turn 'on' access to less secure app for your email
MY_EMAIL = "Dummy email address"
MY_PASSWORD = "Dummy email password"

# Generating OTP
digits = '0123456789'
OTP = ''

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]

otp_msg = OTP + " is your OTP. \nPlease do not share this with anyone."


# Taking user emailid as input
user_email = input("Enter your email: ")


# Emailing the OTP
with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=user_email,
            msg=f"Subject:OTP Verification!\n\n{otp_msg}."
        )


# Verify the OTP
otp_verify = input("Enter the OTP recieved: ")

if otp_verify == OTP:
    print("\nOTP verification seccessfull! :)\n")
else:
    print("\nPlease check your OTP once again :(\n")