"""
This program asks the user for his age then detects ticket cost according to age.
"""

#ticketcost = 0
programrun = "y"
while programrun == "y":
    age = int(input("Enter your age: "))
    if age >0 and age <=5 :
        ticketcost = 0
    elif age >5 and age <=10 :
        ticketcost = 5
    elif age >10 and age <=20:
        ticketcost = 10
    elif age >20 and age <= 100:
        ticketcost = 20
    print(f"The ticket price is {ticketcost}$ \nPress y to continue n to stop")
    programrun = input()
