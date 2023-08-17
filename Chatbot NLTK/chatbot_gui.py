import tkinter as tk
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    

        ChatLog.insert(END, "Bot: " + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 
# Create the main window
base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
base.configure(bg="#f0f0f0")  # Set background color

# Create Chat window with scrollbar
ChatLog = Text(base, bd=0, bg="#f0f0f0", height="8", width="50", font=("Arial", 12))

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#25cdf7", activebackground="#3c9d9b", fg='#ffffff',
                    command=send)

# Create the box to enter message
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font=("Arial", 12))

# Place components on the screen using grid layout
ChatLog.grid(row=0, column=0, columnspan=4, padx=6, pady=6)
scrollbar.grid(row=0, column=4, sticky="ns")
EntryBox.grid(row=1, column=1, columnspan=3, padx=6, pady=6)
SendButton.grid(row=1, column=0, padx=6, pady=6)

# Apply a consistent font color and style to the chat messages
ChatLog.tag_configure("user", foreground="#007bff", font=("Verdana", 12))
ChatLog.tag_configure("bot", foreground="#3c9d9b", font=("Verdana", 12))

def append_message(tag, message):
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, message + '\n', tag)
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

def send_user_message():
    user_message = EntryBox.get("1.0", 'end-1c').strip()
    if user_message:
        append_message("user", "You: " + user_message)
        EntryBox.delete("0.0", END)



# Update button command to call send_user_message
SendButton.configure(command=send_user_message)

# Run the GUI event loop
base.mainloop()
