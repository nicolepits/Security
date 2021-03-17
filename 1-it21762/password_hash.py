import nacl.pwhash

# In this very simple program we use nacl.pwhash library and use the nacl.pwhash.st functin to convert
# the password given by the user to hashed. This function only accepts passwords in bytes so we use the
# encode() function for that and in the end we decode() it to store it in our txt file in string format.

f = open("password_hashes.txt", "a")

while True:
  username = input("Enter username\n")
  if not username:
    f.close()
    break
  password = input("Enter password\n")

  storedpassword = nacl.pwhash.str(password.encode())
  f.write(username)
  f.write(" ")
  f.write(storedpassword.decode())
  f.write("\n")
  print("Data written\n")