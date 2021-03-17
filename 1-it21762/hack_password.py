import nacl.pwhash

# In this program we exclusively use nacl.pwhash library. This is a simple program that reads two files and
# verifies if some of the hashed passwords in the password_hashes.txt match with a popular password. We use 
# the nacl.pwhash.verify for that job and in case the key/password is wrong, the exception is caught and the
# loop continues.

f = open("password_hashes.txt", "r")

for line in f.readlines(): # Read the lines
    
    g = open("popular_passwords.txt", "r")
    for lines in g.readlines():
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        popular = lines.split('\n')
        try:
            result = nacl.pwhash.verify(login_info[1].encode(),popular[0].encode())
            print("Found password.")
            print("Username: ")
            print(login_info[0])
            print("Password: ")
            print(lines)
        
        except nacl.exceptions.InvalidkeyError: 
            pass
        
    g.close()
f.close()