from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
root=Tk()
root.geometry("600x500")
root.title("🥳😰best friends💘💖🥰😱")

label2=Label(root, text="translator", fg="pink", font=("times",32))
label2.place(relx=0.5, rely=0.1, anchor=CENTER)

label3=Label(root, text="enter text", fg="black", font=("times",32))
label3.place(relx=0.1, rely=0.2, anchor=CENTER)

inputbox=Text(root,height=11, width=60)
inputbox.place(relx=0.1, rely=0.3, anchor=CENTER)

output=Text(root,height=11, width=60)
output.place(relx=0.7, rely=0.3, anchor=CENTER)

language=list(LANGUAGES.values())
fruitdropdown=ttk.Combobox(root,value=language)
fruitdropdown.place(relx=0.2, rely=0.1, anchor=CENTER)

outputdropdown=ttk.Combobox(root,value=language)
outputdropdown.place(relx=0.7, rely=0.1, anchor=CENTER)



root.mainloop()