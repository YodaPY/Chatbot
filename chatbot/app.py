from chatbot import chatbot
from tkinter import (
    Tk,
    Frame,
    Label,
    Text,
    Button,
    Scrollbar,
    Entry,
    DISABLED,
    END,
    NORMAL
)

class Window(Frame):
    def __init__(
        self,
        master
    ) -> None:

        self.master = master
    
    def layout(self) -> None: 
        self.master.deiconify() 
        self.master.title("Chatbot") 
        self.master.resizable(
            width = False, 
            height = False
        ) 
        self.master.configure(
            width = 470,
            height = 550, 
            bg = "#17202A"
        )

        self.line = Label(
            self.master,
            width = 450, 
            bg = "#ABB2B9"
        ) 
          
        self.line.place(
            relwidth = 1, 
            rely = 0.07, 
            relheight = 0.012) 
          
        self.text_cons = Text(
            self.master, 
            width = 20,  
            height = 2, 
            bg = "#17202A", 
            fg = "#EAECEE", 
            font = "Helvetica 14",  
            padx = 5, 
            pady = 5
        ) 
          
        self.text_cons.place(
            relheight = 0.745, 
            relwidth = 1,  
            rely = 0.08
        ) 
          
        self.label_bottom = Label(
            self.master, 
            bg = "#ABB2B9", 
            height = 80
        ) 
          
        self.label_bottom.place(
            relwidth = 1, 
            rely = 0.825
        ) 
          
        self.entry_msg = Entry(
            self.label_bottom, 
            bg = "#2C3E50", 
            fg = "#EAECEE", 
            font = "Helvetica 13"
        ) 
          
        self.entry_msg.place(
            relwidth = 0.74, 
            relheight = 0.06, 
            rely = 0.008, 
            relx = 0.011
        ) 
          
        self.entry_msg.focus() 
    
        self.button_msg = Button(
            self.label_bottom, 
            text = "Send", 
            font = "Helvetica 10 bold",  
            width = 20, 
            bg = "#ABB2B9", 
            command = lambda : self.send(self.entry_msg.get())
        ) 
          
        self.button_msg.place(
            relx = 0.77, 
            rely = 0.008, 
            relheight = 0.06,  
            relwidth = 0.22
        ) 
          
        self.text_cons.config(
            cursor = "arrow"
        ) 
          
        scrollbar = Scrollbar(self.text_cons) 
           
        scrollbar.place(
            relheight = 1, 
            relx = 0.974
        ) 
          
        scrollbar.config(
            command = self.text_cons.yview
        ) 
          
        self.text_cons.config(
            state = DISABLED
        )

    def send(self, msg) -> None:
        self.text_cons.config(
            state = DISABLED
        )

        self.entry_msg.delete(0, END)

        self.output(
            msg,
            name="Me"
        )

        self.output(
            chatbot.ask(msg),
            name="Bot"
        )

    def output(self, msg, *, name) -> None:
        self.text_cons.config(
            state = NORMAL
        )

        self.text_cons.insert(END, f"{name}: {msg}\n\n")

        self.text_cons.config(
            state = DISABLED
        ) 
        self.text_cons.see(END)

def run() -> None:
    root = Tk()
    window = Window(root)
    window.layout()

    root.mainloop()