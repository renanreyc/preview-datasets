import os

def listar_arquivos(path, format):
    caminho_da_pasta = path
    formato_arquivo = format

    if not os.path.exists(caminho_da_pasta):
        return "O caminho da pasta não existe."

    arquivos_encontrados = []

    for root, _, files in os.walk(caminho_da_pasta):
        for arquivo in files:
            if arquivo.endswith(formato_arquivo):
                arquivos_encontrados.append(os.path.join(root, arquivo))

    if arquivos_encontrados:
        return arquivos_encontrados
    else:
        return "Nenhum arquivo encontrado."