from tkinter import *
from dbFolder.dbFunctions import nullEscDBClass

database = nullEscDBClass()
database.startDB("mysql.djangosfantasy.com", "djangoadmin8", "best!Group")
root = Tk()
frame = root.geometry("500x400")
# root.configure(bg = "white")
Label(text="Welcome to NullEscape Arcade! Choose Login Or Register", bg="light slate blue", width="500",
                      height="3", justify="left", font=("Helvetica", 18)).pack()
Label(text="Enter Username", bg="white", width="500", height="2", font=("Helvetica", 16)).pack()
usernameentry = Entry(root)
usernameentry.pack()
def getLoginDetails():
    global value
    username = usernameentry.get()
    password = passwordentry.get()
    database.signupUser(username, password)
    print("Username = " + str(username))
    print("Password = " + str(password))
Label(text="Enter Password", bg="white", width="500", height="2", font=("Helvetica", 16)).pack()
passwordentry = Entry(root)
passwordentry.pack()
loginbutton = Button(text="Login",fg = "red", height="2", width="20",command=getLoginDetails)
loginbutton.pack()
signupbutton = Button(text="Sign Up",fg = "red", height="2", width="20")
signupbutton.pack()
Button(root, text="Exit", command=root.quit).pack()
root.mainloop()
