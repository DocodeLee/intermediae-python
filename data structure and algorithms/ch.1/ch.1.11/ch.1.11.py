import math
number = int(input("please enter an int : "))

# try:
#     print(math.sqrt(number))
# except:
#     print("Bad value for square root")
#     print("This result is from abs number")
#     print(math.sqrt(abs(number)))

if number < 0:
    raise RuntimeError("You cannot use negative number")
else:
    print(math.sqrt(number))