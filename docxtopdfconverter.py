"""
Convert a Doc file to pdf using python with GUI
"""
# import libraries
# tkinter is already in python 3.x  so no need of pip
import tkinter as tk
from docx2pdf import convert # pip install docx2pdf
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo

# create tkinter window object
win=tk.Tk()
win.title("Word to Pdf Converter") #window title

def openfile():
    """
    function to convert the file
    :return:
    """
    file=askopenfile(filetypes=[('Word Files','*.docx')])
    convert(file.name,r'C:\Users\prajw\Downloads\converted.pdf') #file path to store the converted pdf file
    showinfo("Done","File successfully converted ")

# create a label
label=tk.Label(win,text="Choose a file")
label.grid(row=0,column=0,padx=5,pady=5)

# create a button
button=ttk.Button(win,text="Select",width=30,command=openfile())
button.grid(row=0,column=1,padx=5,pady=5)

# main loop
win.mainloop()