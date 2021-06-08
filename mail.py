import smtplib
from email.message import EmailMessage

def sendmail(mail, pswd, sendTo, subject, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(mail, pswd)
    email=EmailMessage()
    email["From"]=mail
    email["To"]=sendTo
    email["Subject"]=subject
    email.set_content(message)
    server.send_message(email)
    #server.sendmail(mail, sendTo,message)
