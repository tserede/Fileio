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
    history=[] #изначально  history- это пустой список для хвранения истории. Затем туда будем добавлять
    #c информацией  о имени файла и ссылке, по которой можно скачать
    if os.path.exists(history_file): # проверяем, что файл, путь к файлу существует
        with open(history_file, 'r') as f:  # если он существует, открываем его для чтения
            history=json.load(f) #далее в переменную history загружаем то, что уже есть в нашем файле. Если он пустой, то ничего не загрузим, но  если там что-то было, то мы в переменную
            #history их загрузим и потом сможем их туда добавить с помощью append информацию
    history.append({"file_path": os.path.basename(file_path), "download_link": link}) # добавляем в history новые загруженные путь и ссылка
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)



def upload():
    try:
        filepath=fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files={'file': f}
                response=requests.post('http://file.io', files=files)
                response.raise_for_status()
                link=response.json()['link']
                entry.delete(0,END)
                entry.insert(0,link)
                pyperclip.copy(link) #ссылка отправлена в буфер обмена.
                save_history(filepath, link)
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
