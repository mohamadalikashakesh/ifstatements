"""
This Program asks the user to enter a number and checks if even or odd.
"""

programrun = "y"
while programrun == "y":
    num=int(input("Enter a number: "))
    if(num%2 == 0):
        print("The Number is Even")
    else:
        print("The Number is Odd")
    print("Enter y to Continue n to stop")
    programrun = input()