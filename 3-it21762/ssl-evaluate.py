import socket
import ssl
import datetime
import sys

# In this program we evaluate www.hua.gr's SSL certificate using the ssl and socket library.
# We create a connection to the socket and connect to 443 port where the SSL exists. getpeercert()
# function is then used to retrieve the certificate dictionary. Finally while doing the correct
# conversions we evaluate each requested field of the certificate.

print("*" * 50)
print("Evaluating www.hua.gr's SSL certificate...")
print("*" * 50)

hostname = 'www.hua.gr'
ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, 443))
    cert = s.getpeercert()

    issuer = cert['issuer']  #get all cert's fields that we wish
    subject = cert['subject']
    not_before = cert['notBefore']
    not_after = cert['notAfter']
    
    timestamp_before = ssl.cert_time_to_seconds(not_before) #get SSL's date in microseconds since EPOCH
    timestamp_after = ssl.cert_time_to_seconds(not_after)

    format = r'%Y-%m-%d %X' #the format of the datetime objects we want to compare

    before_time = datetime.datetime.utcfromtimestamp(timestamp_before) #convert the SSL microseconds to datetime object
    after_time =datetime.datetime.utcfromtimestamp(timestamp_after)

    answer = input("Would you like to evaluate SSL's date with:\n1.Current date\n2.My date\nEnter 1 or 2\n")
    if '1' in answer :
        current_date = datetime.datetime.now() #get current date
    
        date =  datetime.datetime.strptime(current_date.strftime(format),format) #convert to the format 
        
    elif '2' in answer :
        try:
            tmp_date = input("Input date using strictly the format: YYYY-MM-DD hh:mm:ss\n")
            date =  datetime.datetime.strptime(tmp_date,format) #This converts the date sting to datetime
        except ValueError:
            print("Wrong date values! Exiting...")
            sys.exit()
    else :
        print("Wrong input")
        sys.exit()  #the program exits

    #validate date by comparing
    if date>before_time and date<after_time:
        print("SSL's date validated")
    else: 
        print("SSL's date is not valid")

    #validate version
    ver = cert['version']
    if ver == 3:
        print("SSL's version is '3'")

    #validate commonName of issuer
    issuer_tmp = input("> Enter the common name of SSL issuer\n")

    if issuer_tmp in str(issuer[4]) : 
        print("SSL issuer validated") #answer: TERENA SSL CA 3
    else :
        print("SSL issuer invalid")

    subject_tmp = input("> Enter the common name of SSL subject\n")

    if subject_tmp in str(subject[5]) :
        print("SSL subject validated") #answer: *.hua.gr
    else :
        print("SSL subject invalid")

    