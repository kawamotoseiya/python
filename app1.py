import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")

def dispLabel():
    lbl.configure(text="こんにちは")
    
import tkinter as tk
root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)
lbl.pack()
btn.pack()
tk.mainloop()
