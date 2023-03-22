import tkinter as tk

import customtkinter


class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)
    def return_value(self, value):
        self.master.return_value = value
        self.master.destroy()

def get_user_input():
    root = tk.Tk()
    root.geometry("200x100")
    root.title("Input Demo")

    # Definindo a função que será executada quando o botão for clicado
    def on_button_click():
        custom_button.return_value(entry.get())

    # Criando a entrada e o botão personalizado
    entry = tk.Entry(root)
    entry.pack(pady=10)
    custom_button = CustomButton(root, text="OK", command=on_button_click)
    custom_button.pack(pady=10)

    # Iniciando a janela principal e esperando pelo retorno de valor
    root.return_value = None
    root.mainloop()

    # Retornando o valor após a janela ser fechada
    return root.return_value

# Chamando a função para obter entrada do usuário
user_input = get_user_input()

# Exibindo a entrada do usuário salva em uma variável fora da função
print("O usuário digitou:", user_input)