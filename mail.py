import smtplib
from email.message import EmailMessage
from tkinter import messagebox
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as mic:
        print("Listening..")
        voice = listener.listen(mic)
        data = listener.recognize_google(voice)
        print(data)
        print("Done")
except:
    pass


def login(mailId, password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(mailId, password)
        return True
    except:
        return False


def sendmail(mailId, password, sendTo, subject, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(mailId, password)
    except:
        messagebox.showinfo("Error", "Please Enter Valid details")
    email = EmailMessage()
    email["From"] = mailId
    email["To"] = sendTo
    email["Subject"] = subject
    email.set_content(message)
    try:
        server.send_message(email)
        messagebox.showinfo("Error", "Email Sent Successfully")
    except:
        messagebox.showinfo("Error", "Email couldn't be sent")
    # server.sendmail(mail, sendTo,message)
