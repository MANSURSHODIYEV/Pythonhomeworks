password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short")
elif not any(char.isupper() for char in password):
    print("Password must contain an upprcase letter.")
else:
    print("Password is strong.")