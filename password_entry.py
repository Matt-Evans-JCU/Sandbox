""" Matt Evans """

password = input("Pick a password: ")
while len(password)<6:
    print("Password not long enough")
    password = input("Pick another password: ")
print('*'*len(password))