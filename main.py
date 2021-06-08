from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from functions import *
import smtplib

# root panel and frames
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def showFrame(frame):
    frame.tkraise()  # to raise the required frame


frame1 = Frame(root)  # login frame
frame2 = Frame(root)  # choose options
frame3 = Frame(root, bg="black")  # voice mail
frame4 = Frame(root, bg="blue")  # send mail
frame5 = Frame(root, bg="red")  # check inbox

for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, sticky="nsew")
showFrame(frame1)

root.title("GC Mail Client")
root.iconphoto(False, PhotoImage(file='images/email.png'))
root.geometry("1000x600")
root.resizable(0, 0)

# labels-Frame1
titleLabel1 = Label(frame1, text="GC Mail Client", font=('Calibri', 50))
titleLabel2 = Label(frame1, text="A voice based mail client", font=('Calibri', 25))
label1 = Label(frame1, text="Mail : ", font=('Calibri', 20))
label2 = Label(frame1, text="Password : ", font=('Calibri', 20))
emptyLabel = Label(frame1, text="   ", font=('Calibri', 20))

# entries-Frame1
mailEntry = Entry(frame1, width=25)
pswdEntry = Entry(frame1, width=25)


# button functions-Frame1
# mailId = ""
# password = ""
def letsGo():
    mailId = mailEntry.get()
    password = pswdEntry.get()
    if mailId == "" or password == "":
        messagebox.showinfo("Error", "Please Enter the details")
    else:
        tempLabel = Label(frame1, text=mailId)
        tempLabel.grid(row=5, column=1)
        showFrame(frame2)


# buttons-Frame1
letsGoButton = Button(frame1, text="Lets Go", font=('Calibri', 15), command=letsGo)

# show on Frame1
emptyLabel.grid(row=0, column=0, padx=135)
titleLabel1.grid(row=0, column=1, columnspan=3)
titleLabel2.grid(row=1, column=1, columnspan=3)
emptyLabel.grid(row=2, pady=35)
label1.grid(row=3, column=1)
label2.grid(row=4, column=1)

mailEntry.grid(row=3, column=2, pady=7)
pswdEntry.grid(row=4, column=2, pady=7)

letsGoButton.grid(row=5, column=2)


# button functions-Frame2
def f1():
    showFrame(frame3)


def f2():
    showFrame(frame4)


def f3():
    showFrame(frame5)


# Buttons And Labels-Frame2
photo1 = PhotoImage(file="images/voice.png")
photo2 = PhotoImage(file="images/typing.png")
photo3 = PhotoImage(file="images/inbox.png")
imgbutton1 = Button(frame2, text="Send Mail Through Voice Commands", image=photo1, compound=TOP, command=f1)
imgbutton2 = Button(frame2, text="Send General Mail", image=photo2, compound=TOP, command=f2)
imgbutton3 = Button(frame2, text="Check Inbox", image=photo3, compound=TOP, command=f3)
emptyLabel = Label(frame2, text="   ", font=('Calibri', 20))

# show on Frame2
emptyLabel.grid(row=0, column=0, padx=20)
emptyLabel.grid(row=2, pady=35)
imgbutton1.grid(row=3, column=1, padx=4)
imgbutton2.grid(row=3, column=2, padx=4)
imgbutton3.grid(row=3, column=3, padx=4)

# backbuttons
backbutton1 = Button(frame3, text="Back", command=lambda: showFrame(frame2))
backbutton2 = Button(frame4, text="Back", command=lambda: showFrame(frame2))
backbutton3 = Button(frame5, text="Back", command=lambda: showFrame(frame2))
backbutton1.grid(row=0)
backbutton2.grid(row=0)
backbutton3.grid(row=0)

# end
root.mainloop()
