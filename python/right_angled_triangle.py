num = int(input("Enter a number"))

print("Right angled triangle of size {} :".format(num))
for  i in range(1, num+1):
    print("*" * i)

print("Inverted Right angled triangle of size {} :".format(num))
i = num
while(i != 0):
    print("*" * i)
    i -= 1
