import smtplib

to= input("enter the email address of the receiver")
message=input("enter the message")
def  sendEmail(to,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #add the senders email address and pass in the below fields
    server.login('senderemail','password')
    server.sendmail(senderemail,to,message)
    server.close()
    
sendEmail(to,message)