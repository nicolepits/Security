
import sys 
import socket 
from datetime import datetime 
   
# In this program we basically use Python's socket library to connect to a socket, and try to connect
# to each port with the socket's connect() function. There is a for getting all port ranging from 1 to
# 100. This program is in reality slow at reading all ports , one way of making this program faster is
# to use multithreading techniques.
# The banner is retrieved once the port is open using the recv function.


#Main program starts now

print("PORT SCANNER") 

f = open("addresses.txt", "r")

for line in f.readlines():
    #get ip from line
    ip = line.split("\n") #remove \n from the string
    
    try:
        target = socket.gethostbyname(ip[0])  # translate hostname to IPv4
    except:
        print("Could not be reached IP : ", ip[0])
        break
    # Add Banner  
    print("*" * 50) 
    print("Scanning Target: " + target) 
    print("Scanning started at:" + str(datetime.now())) 
    print("*" * 50) 

    for port in range(1,100):

        print("Knock on port: ", port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((target, port))
            print("Port is open!")
            banner = s.recv(2048)
            print(banner)
        except KeyboardInterrupt: 
                print("\n Goodbye!") 
                sys.exit() 
        except socket.gaierror: 
                print("\n Hostname could not be resolved.") 
                sys.exit() 
        except Exception as e:
            print(e)          
        except 10060:
            pass
        
        

f.close()