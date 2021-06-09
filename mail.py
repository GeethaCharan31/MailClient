import smtplib
from email.message import EmailMessage

def sendmail(mailId, password, sendTo, subject, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(mailId, password)
    email=EmailMessage()
    email["From"]=mailId
    email["To"]=sendTo
    email["Subject"]=subject
    email.set_content(message)
    server.send_message(email)
    #server.sendmail(mail, sendTo,message)
