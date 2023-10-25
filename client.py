from tkinter import*
import socket

from threading import Thread

client = socket.sockset(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("connectes with server")

class GUI : 
    def _init__(self):
        self.Window = TK()
        self.Window.withdraw()


        self.login = Toplevel()
        self.login.title("login")

        self.login.resizable(width = False, height = False)
        self.login.configure(width = 400, height = 300)

        self.pls =  Lable(self.login,
            text = "Please login to continue",
            justify = CENTER,
            font = "helvetica 14 bold"

        )

        
        self.pls.place(relHeight = 0.15, 
        relX = 0.2,
        relY = 0.007 )

        self.LableName.place(relHeight = 0.2,
        relX = 0.1, 
        relY = 0.2)
        
       self.entryName = Entry(self.login,
							font = "Helvetica 14"
                            )

        self.entryName.place = (relHeight = 0.12, relWidth = 0.4
        relX = 0.35, relY = 0.2)

        self.entryName.focus()
        
        self.go = Button(self.login, 

        text = "continue",
        font = "helvetica 14 bold"
        
        )



