from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import sqlite3
import os

def doNothing():
    pass

root = tk.Tk()

width = 1200
height = 800
itemPadx = 10
itemPady = 10

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

dimension = f"{width}x{height}+{x}+{y}"

root.geometry(dimension)
root.title("Main")
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)

#######################################################################################################
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=doNothing)
filemenu.add_command(label="Clear All", command=doNothing)
filemenu.add_command(label="Settings", command=doNothing)
filemenu.add_command(label="Exit", command=doNothing)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Add", command=doNothing)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

#######################################################################################################
generalFont = tkFont.Font(family="Arial", size=10, weight="bold")
#######################################################################################################

def getfile():
    filePath = filedialog.askdirectory()
    if filePath:
        current_dir.set(filePath)
        labelpath.config(state='normal')
        labelpath.delete(0, tk.END)
        labelpath.insert(0, filePath)
        labelpath.config(state='readonly')
        listFiles(filePath)
        print(f"directory: {filePath} — {current_dir.get()}")

def listFiles(folder_path):
    listboxItems.delete(0, tk.END)
    for name in os.listdir(folder_path):
        listboxItems.insert('end', name)

def removeSelected():
    selectedItem = listboxItems.curselection()
    for index in reversed(selectedItem):
        listboxItems.delete(index)

def addItems():
    addFile = filedialog.askopenfiles()
    for file in addFile:
        filename = os.path.basename(file.name)
        listboxItems.insert('end', filename)

def clearAll():
    listboxItems.delete(0, tk.END)

def showMessageBox():
    selectedItem = listboxItems.curselection()
    if selectedItem:
        messagebox.showinfo("Main", f"Path:{current_dir.get()}{listboxItems.get(selectedItem)}")
    else:
        messagebox.showerror("Error", "No item selected")

current_dir = tk.StringVar()

#######################################################################################################

leftframe = tk.LabelFrame(root, text="Convert Files", labelanchor="n", font=generalFont)
leftframe.grid(row=0, column=0, padx=itemPadx, pady=itemPady, ipadx=5, ipady=5, sticky="NSEW")

leftframe.columnconfigure(0, weight=1)
leftframe.columnconfigure(1, weight=0)
leftframe.rowconfigure(0, weight=0)
leftframe.rowconfigure(1, weight=0)
leftframe.rowconfigure(2, weight=0)

lf_buttonFrame = tk.Frame(leftframe)
lf_buttonFrame.grid(row=1, column=1, sticky="NSEW", padx=itemPadx, pady=itemPady)

centerframe = tk.LabelFrame(root, text="Count", labelanchor="n", font=generalFont)
centerframe.grid(row=0, column=1, padx=itemPadx, pady=itemPady, sticky="NSEW")

rightframe = tk.LabelFrame(root, text="Converted", labelanchor="n", font=generalFont)
rightframe.grid(row=0, column=2, padx=itemPadx, pady=itemPady, sticky="NSEW")

#######################################################################################################
entryValue = StringVar()
labelpath = tk.Entry(leftframe, text="Path://", state='readonly', readonlybackground="white", fg="black",bd=1, wraplength=None, relief="solid", justify="left", font=generalFont, width=15, textvariable=entryValue)
labelpath.grid(row=0, column=0, padx=itemPadx, pady=itemPady, sticky="NSEW")

buttonbrowse = tk.Button(leftframe, text="Browse", height=1, bd=1, relief="solid", font=generalFont, command=getfile)
buttonbrowse.grid(row=0, column=1, padx=itemPadx, pady=itemPady, sticky="NSEW")

listboxItems = tk.Listbox(leftframe, bg="white", fg="black", bd=1, relief="solid", font=generalFont, selectmode="multiple")
listboxItems.grid(row=1, column=0, sticky="NSEW", padx=itemPadx, pady=itemPady)

buttonAddItem = tk.Button(lf_buttonFrame, text="Add", height=1, bd=1, relief="solid", font=generalFont, command=addItems).grid(row=0, column=0, sticky="NEW", pady=(0, itemPady))
buttonRemoveItem = tk.Button(lf_buttonFrame, text="Remove", height=1, bd=1, relief="solid", font=generalFont, command=removeSelected).grid(row=1, column=0, sticky="NEW", pady=(0, itemPady))
buttonRemoveAllItem = tk.Button(lf_buttonFrame, text="Remove All", height=1, bd=1, relief="solid", font=generalFont, command=clearAll).grid(row=2, column=0, sticky="NEW", pady=(0, itemPady))
buttonShow = tk.Button(lf_buttonFrame, text="Test", height=1, bd=1, relief="solid", font=generalFont, command=showMessageBox).grid(row=3, column=0, sticky="NEW", pady=(0, itemPady))

root.mainloop()