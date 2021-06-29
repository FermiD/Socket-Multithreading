# -*- coding: utf-8 -*-

from tkinter import *
from chat import get_response, bot_name
import client
import server

#ui colors and font -> 12-17
BG_GRAY = "ABB2B9"
BG_COLOR = "#00008B"
TEXT_COLOR = "#EAECEE"

FONT = "Arial"
FONT_BOLD = "Arial Bold"

class ChatApp:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("CHAT")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        #head
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        #border
        line = Label(self.window, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #text tool
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #scroll
        scrollbar= Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.975)
        scollbar.configure(command=self.text_widget.yview)
        
        #bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        #messaging thing
        self.messenger = Entry(bottom_label, bg="#006400", fg=TEXT_COLOR, font=FONT)
        self.messenger.place(relwidth=0.74, relheight=0.6, rely=0.008, relx=0.011)
        self.messenger.focus()
        self.messenger.bind("<Return>", self.on_enter_pressed)
        
        #send messagebtn
        send_button = Button(bottom_label, text="Send", font="FONT_BOLD", width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely= 0.008, relheight=0.06, relwidth=0.22)
        
        #self explanatory
    def _on_enter_pressed(self, event):
        msg = self.messenger.get()
        self._insert_message(msg, "You")
        
        #the chat process
    def _insert_message(self, send, start):
        if not msg:
            return
        self.messenger.delete(0, END)
        msg1 = f"{start}: {send}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
        
if __name__ == "__main__":
    app = ChatApp()
    app.run()