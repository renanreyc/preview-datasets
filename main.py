import os
import tkinter as tk
from tkinter import OptionMenu
from tkinter import ttk

from src import list_files, report_files

def reportar_arquivos():
    if not isinstance(list_files_result, str):
        path_save = save_path.get()
        format_file =  formato_var.get()

        result_report_files = report_files.handle_files(list_files_result, path_save, format_file, resultado_report)

        if isinstance(result_report_files, str):
            resultado_report.insert("end", result_report_files)

def listar_arquivos():
    path =  entrada_caminho.get()
    format_file =  formato_var.get()

    global list_files_result  # Precisamos declarar list_files_result como global para acessá-lo em outras funções
    list_files_result = list_files.listar_arquivos(path, format_file)

    # Limpa a caixa de texto antes de exibir o novo resultado
    resultado.delete("1.0", "end")

    if isinstance(list_files_result, str):
            resultado.insert("end", list_files_result)
    else:
        qtd_files = len(list_files_result)
        resultado.insert("end", f"{qtd_files} arquivos encontrados.\n\n")

        for arquivo in list_files_result:
            resultado.insert("end", arquivo + "\n")

    

# Configuração da janela principal
janela = tk.Tk()
janela.title("Preview datasets")
janela.geometry("1200x800")

# Rótulo e entrada para o caminho da pasta
label_caminho = tk.Label(janela, text="Caminho da Pasta:", font=("Arial", 16))
label_caminho.pack()

#entrada caminho
entrada_caminho = tk.Entry(janela, width=80)
entrada_caminho.pack()

# Adicione um espaço vazio (Label vazia) para criar espaço entre o rótulo e o menu
espaco_vazio = tk.Label(janela, text="")
espaco_vazio.pack()

# Rótulo para a lista de opções
label_formato = tk.Label(janela, text="Selecione o Formato do Arquivo:", font=("Arial", 16))
label_formato.pack()

# Opções disponíveis no menu suspenso
opcoes_formato = [".xlsx", ".csv", ".parquet"]

# Variável de controle para armazenar a opção selecionada
formato_var = tk.StringVar()
formato_var.set(opcoes_formato[0])  # Defina a opção padrão

# Estilo personalizado para o OptionMenu
style = ttk.Style()
style.configure("TMenubutton", padding=(20, 20))  # Aumenta o tamanho do menu flutuante

# Crie o menu suspenso com as opções
menu_formato = OptionMenu(janela, formato_var, *opcoes_formato)
menu_formato.config(width=40, anchor="w")
menu_formato.pack()

# Adicione um espaço vazio (Label vazia) para criar espaço entre o rótulo e o menu
espaco_vazio = tk.Label(janela, text="")
espaco_vazio.pack()

# Botão para listar os arquivos
botao_listar = tk.Button(janela, text="Listar Arquivos", command=listar_arquivos, width=40, bg="#8ed49f")
botao_listar.pack()

path =  entrada_caminho.get()
format_file =  formato_var.get()
list_files_result = list_files.listar_arquivos(path, format_file)

# Área de resultado
resultado = tk.Text(janela, wrap=tk.WORD, width=100, height=10)
resultado.pack()

# Adicione um espaço vazio (Label vazia) para criar espaço entre o rótulo e o menu
espaco_vazio = tk.Label(janela, text="")
espaco_vazio.pack()

# Rótulo e entrada para o caminho da pasta
save_label_path = tk.Label(janela, text="Caminho para Salvar Arquivos", font=("Arial", 16))
save_label_path.pack()

#save caminho
save_path = tk.Entry(janela, width=80)
save_path.pack()

# Adicione um espaço vazio (Label vazia) para criar espaço entre o rótulo e o menu
espaco_vazio = tk.Label(janela, text="")
espaco_vazio.pack()

# Botão para gerar Report
botao_report = tk.Button(janela, text="Gerar Reporte de Arquivos", command=reportar_arquivos, width=40, bg="#d48e8e")
botao_report.pack()

# Área de resultado do relatório
resultado_report = tk.Text(janela, wrap=tk.WORD, width=100, height=10)
resultado_report.pack()

janela.mainloop()