from tkinter import *
from tkinter import filedialog
from main import *
import tkinter as tk
import os

def abrir_pasta():
    folder_path = filedialog.askdirectory()  # Open a folder selection dialog
    if folder_path:
        tela_seleção(root, folder_path)

def procurar_lista(entry, lista):
    pass

def carregar_lista(lista):
    lista.delete(0, tk.END)  # Clear the Listbox
    for item in arquivos_salvos:
        lista.insert(tk.END, item)  # Insert folder contents into Listbox

#####################################

def tela_inicial(root):
    label = Label(root, text='Listador de Músicas',font=('Rosewood Std Regular', 30))
    label.pack(padx=5, pady=25, anchor=tk.CENTER)
    texto = tk.Label(root, text="Um pequeno programa que lista \n todas as suas músicas dentro de uma pasta.", font=(25))
    texto.pack()
    texto2= tk.Label(root, text="Funciona apenas com arquivos '.ogg' e '.mp4'.", font=(25))
    texto2.pack(pady=30)
    button_abrir_pasta = tk.Button(root, text="Abrir Pasta", font=(40) ,command=lambda:abrir_pasta())
    button_abrir_pasta.pack(padx=5, pady=110, anchor=tk.CENTER)


def tela_seleção(root, folder_path):
    for widget in root.winfo_children():
        widget.destroy()
    label = Label(root, text='Listador de Músicas' ,font=('Rosewood Std Regular', 30))
    label.pack(padx=5, pady=5, anchor=tk.CENTER)
    lista = tk.Listbox(root, selectmode=tk.SINGLE, height= 20, width= 40)
    lista.pack(pady=10)
    entry_texto = tk.Label(root, text="Digite o nome da música")
    entry_texto.pack(pady=10)
    entry_musica = tk.Entry(root, width=30)
    entry_musica.pack(pady=5)
    btn_adicionar = tk.Button(root, text="Procurar na Lista", command=lambda:procurar_lista(entry_musica, lista))
    btn_adicionar.pack(pady= 10)

    nomear_arquivos(folder_path)
    print(arquivos_salvos)
    carregar_lista(lista)

root = tk.Tk()
root.title("Listador de Arquivos")
root.geometry("600x600")
tela_inicial(root)
root.mainloop()