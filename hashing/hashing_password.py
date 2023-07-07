import bcrypt

pw = "Exampl3password"

# salt -> generate

hashed_pw = bcrypt.hashpw(pw.encode(),bcrypt.gensalt()).decode()

#print(hashed_pw)

given = input("enter your password: ")

if bcrypt.checkpw(given.encode(), hashed_pw.encode()):
    print("Password match!")
else:
    print("Unauthorized!")
