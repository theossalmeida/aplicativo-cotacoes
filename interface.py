import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date, timedelta
from funcoes import *


# Função que recebe os parâmetros e preenche os campos
def preencher_campos(moeda, data):
    campo1_entrada.delete(0, tk.END)  # Limpa o campo 1
    campo2_entrada.delete(0, tk.END)  # Limpa o campo 2
    campo3_entrada.delete(0, tk.END)  # Limpa o campo 3

    campo1_entrada.insert(0, buscaValorCompra(moeda, data))  # Preenche o campo 1 com o primeiro parâmetro
    campo2_entrada.insert(0, buscaValorVenda(moeda, data))  # Preenche o campo 2 com o segundo parâmetro
    campo3_entrada.insert(0, buscaDataHoraCotacao(moeda, data))


# Função para lidar com o botão pressionado
def enviar_parametros():
    moeda = entrada_param1.get()
    data = cal.get_date()

    preencher_campos(moeda, data)


def data_selecionada():
    data = cal.get_date()


# Cria a janela principal
janela = tk.Tk()
janela.title("Informações sobre cotação")

# Cria rótulos e entradas para os parâmetros
label_param1 = tk.Label(janela, text="Moeda:")
label_param1.grid(row=0, column=0, pady=5)


opcoes_moeda = buscaMoedas()
entrada_param1 = ttk.Combobox(janela, values=opcoes_moeda)
entrada_param1.grid(row=0, column=1, pady=5)


# Cria a entrada de data com o calendário
cal = Calendar(janela, selectmode="day", date_pattern="dd-mm-yyyy", maxdate=(date.today() - timedelta(1)))
cal.grid(row=1, column=1, padx=5, pady=5)
cal.bind("<<CalendarSelected>>", lambda e: data_selecionada())


# Cria um botão para enviar os parâmetros
botao_enviar = tk.Button(janela, text="Buscar", command=enviar_parametros, pady=2)
botao_enviar.grid(row=3, column=1, pady=5)
botao_enviar.config(background="light blue")


# Cria campos de texto para exibir os resultados
campo1_label = tk.Label(janela, text="Valor de compra:")
campo1_label.grid(row=5, column=0, pady=5)

campo1_entrada = tk.Entry(janela)
campo1_entrada.grid(row=5, column=1, pady=5)


campo2_label = tk.Label(janela, text="Valor de venda:")
campo2_label.grid(row=6, column=0, pady=5)

campo2_entrada = tk.Entry(janela)
campo2_entrada.grid(row=6, column=1, pady=5)


campo3_label = tk.Label(janela, text="Data e hora da cotação:")
campo3_label.grid(row=7, column=0, pady=5)

campo3_entrada = tk.Entry(janela)
campo3_entrada.grid(row=7, column=1, pady=5)
