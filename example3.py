"""
This Program asks the user for username and password until correct admin previliges are met 
"""

Access = False
while Access == False:
    Username = input("Enter Username: ")
    PassWord = input("Enter Password: ")
    if Username == "admin" and PassWord == "1234":
        print("Access granted ")
        Access = True
    else:
        Access = False
        print("Access denied")
