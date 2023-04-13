from tkinter import *
from tkinter import ttk

root = Tk()

# Criar a tabela
tabela = ttk.Treeview(root, columns=("col1", "col2", "col3", "col4", "col5"))
tabela.heading("#0", text="ID")
tabela.heading("col1", text="Coluna 1")
tabela.heading("col2", text="Coluna 2")
tabela.heading("col3", text="Coluna 3")
tabela.heading("col4", text="Coluna 4")
tabela.heading("col5", text="Coluna 5")
tabela.column("#0", width=50)
tabela.column("col1", width=150)
tabela.column("col2", width=150)
tabela.column("col3", width=150)
tabela.column("col4", width=150)
tabela.column("col5", width=150)

# Inserir uma linha na tabela
linha1 = tabela.insert("", "end", text="1", values=("Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5"))

# Exibir a tabela na janela
tabela.grid(column=0, row=0)

# Permitir a edição dos valores das células
def on_edit(event):
    # Obter a linha e a coluna da célula que foi editada
    linha = tabela.focus()
    coluna = tabela.identify_column(event.x)
    if coluna != "#0":  # Ignorar a coluna de ID
        # Obter o valor atual da célula
        valor_atual = tabela.item(linha)["values"][int(coluna[3:]) - 1]
        # Criar uma caixa de entrada de texto para o usuário editar o valor
        entrada = Entry(root)
        entrada.insert(0, valor_atual)
        # Exibir a caixa de entrada de texto na posição da célula
        tabela.column(coluna, edit=True)
        tabela.update()
        celula = tabela.identify_cell(event.x, event.y)
        x, y, width, height = tabela.bbox(celula)
        entrada.place(x=x, y=y, width=width, height=height)
        # Definir o foco na caixa de entrada de texto
        entrada.focus_set()
        # Atualizar o valor da célula quando o usuário terminar de editar
        def on_focus_out(event):
            novo_valor = entrada.get()
            tabela.set(linha, coluna, novo_valor)
            entrada.destroy()
        entrada.bind("<FocusOut>", on_focus_out)

tabela.bind("<Double-Button-1>", on_edit)

