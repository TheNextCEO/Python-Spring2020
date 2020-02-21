from tkinter import *
def tkinter_mainwindow():
    root = Tk()
    root.title('Login_page')

def login_page(tk):
    window=Canvas(tk, height=1400, width=1400)
    window.pack(fill="both", expand=True)
    msg1 =Label(window, text='Login before you start')
    msg1.pack(pady=10)
    user_login=Button(window, text='Login', height="2",width="25")
    user_resig=Button(window, text='Register',height="2",width="25")
    user_login.pack(pady=10)
    user_resig.pack(pady=10)

if __name__=='__main__':
    login_page()
mainloop()