from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from tkinter import messagebox as mb
import pyperclip
import json
import os

history_file="upload_history.json" #Это файл с историей загрузок

def save_history(file_path, link):
def upload():
    try:
        filepath=fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files={'file': f}
                response=requests.post('http://file.io', files=files)
                response.raise_for_status()
                link=response.json()['link']д
                entry.delete(0,END)
                entry.insert(0,link)
                pyperclip.copy(link) #ссылка отправлена в буфер обмена.
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


window=Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")
button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry=ttk.Entry()
entry.pack()

window.mainloop()
