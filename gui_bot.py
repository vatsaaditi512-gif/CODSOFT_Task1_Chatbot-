import tkinter as tk
from tkinter import scrolledtext
from advanced_bot import find_response

def send():
    user = entry.get().strip()
    if not user:
        return
    chat_box.configure(state='normal')
    chat_box.insert(tk.END, "You: " + user + "\n")
    bot_resp = find_response(user)
    chat_box.insert(tk.END, "Bot: " + bot_resp + "\n\n")
    chat_box.configure(state='disabled')
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("RuleBot GUI")

chat_box = scrolledtext.ScrolledText(root, state='disabled', width=60, height=20)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side='left', padx=(10,0), pady=(0,10))
send_btn = tk.Button(root, text="Send", command=send)
send_btn.pack(side='left', padx=10, pady=(0,10))

root.mainloop()
