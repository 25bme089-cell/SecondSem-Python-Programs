# Predefined credentials
username = "admin"
password = "1234"

attempts = 0

while attempts < 3:
    try:
        u = input("Enter username: ")
        p = input("Enter password: ")

        if u == username and p == password:
            print("Welcome to the system")
            break
        else:
            attempts += 1
            print("Invalid credentials. Attempts left:", 3 - attempts)

    except Exception as e:
        print("Error:", e)

if attempts == 3:
    raise Exception("Account Locked")
