import tkinter as tk
from tkinter import ttk
from cachorro import Cachorro
from gato import Gato

# Lista global para armazenar os animais cadastrados
animais = []

# Função para cadastrar um animal (Cachorro ou Gato)
def cadastrar_animal():
    nome = nome_entry.get()
    idade = idade_entry.get()
    tipo_animal = tipo_var.get()

    if tipo_animal == "Cachorro":
        porte = atributo_entry.get()
        animal = Cachorro(nome, idade, porte)
    elif tipo_animal == "Gato":
        raca = atributo_entry.get()
        animal = Gato(nome, idade, raca)
    
    animais.append(animal)
    atualizar_lista()

# Função para atualizar a lista de animais cadastrados
def atualizar_lista():
    lista_animais.delete(0, tk.END)
    for animal in animais:
        lista_animais.insert(tk.END, animal.mostrar())

# Função para trocar o campo de atributo de acordo com o tipo de animal
def atualizar_atributo():
    tipo_animal = tipo_var.get()
    if tipo_animal == "Cachorro":
        atributo_label.config(text="Porte:")
    else:
        atributo_label.config(text="Raça:")

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Animais")

# Criação das abas (tabs)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Aba de Cadastro
aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text="Cadastro de Animais")

# Aba de Lista de Animais
aba_lista = ttk.Frame(notebook)
notebook.add(aba_lista, text="Lista de Animais")

# Widgets para a aba de Cadastro
tk.Label(aba_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
nome_entry = tk.Entry(aba_cadastro)
nome_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(aba_cadastro, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
idade_entry = tk.Entry(aba_cadastro)
idade_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(aba_cadastro, text="Tipo:").grid(row=2, column=0, padx=10, pady=10)
tipo_var = tk.StringVar(value="Cachorro")
tipo_menu = ttk.Combobox(aba_cadastro, textvariable=tipo_var, values=["Cachorro", "Gato"])
tipo_menu.grid(row=2, column=1, padx=10, pady=10)
tipo_menu.bind("<<ComboboxSelected>>", lambda event: atualizar_atributo())

atributo_label = tk.Label(aba_cadastro, text="Porte:")
atributo_label.grid(row=3, column=0, padx=10, pady=10)
atributo_entry = tk.Entry(aba_cadastro)
atributo_entry.grid(row=3, column=1, padx=10, pady=10)

# Botão para cadastrar
btn_cadastrar = tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_animal)
btn_cadastrar.grid(row=4, columnspan=2, padx=10, pady=10)

# Widgets para a aba de Lista de Animais
lista_animais = tk.Listbox(aba_lista, width=50, height=10)
lista_animais.pack(padx=10, pady=10)

# Iniciar a interface
root.mainloop()
