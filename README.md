# Aplicação para Gerar Relatórios de Datasets

Este é um projeto Python com interface gráfica usando a biblioteca Tkinter. A aplicação permite listar arquivos em um diretório com base no formato selecionado e gerar relatórios em formato HTML a partir desses arquivos.

## Requisitos

Certifique-se de que você tenha Python 3.x instalado em seu sistema. Além disso, é recomendável criar um ambiente virtual Python para isolar as dependências do projeto. Você pode criar um ambiente virtual usando o seguinte comando:

```bash
python -m venv venv
```

Em seguida, ative o ambiente virtual:

- No Windows (Command Prompt):

```bash
venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

Instale as dependências do projeto listadas no arquivo requirements.txt usando o comando pip:

```bash
pip install -r requirements.txt
```

## Como usar

> 1. Você será apresentado a uma interface gráfica onde pode fazer o seguinte:
>
> - Insira o caminho da pasta que deseja listar arquivos.
> - Selecione o formato dos arquivos que deseja listar a partir do menu suspenso.
> - Clique no botão "Listar Arquivos" para listar os arquivos no diretório selecionado.
>
> 2. A lista de arquivos será exibida na caixa de texto da interface.
>
> 3. Insira o caminho para salvar os relatórios na caixa de texto "Caminho para Salvar Arquivos".
>
> 4. Selecione o formato dos arquivos que deseja gerar relatórios a partir do menu suspenso.
> 
> 5. Clique no botão "Gerar Relatório de Arquivos" para gerar relatórios em HTML para os arquivos.
>
> 6. Os relatórios gerados serão exibidos na caixa de texto "Resultado do Relatório".

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Abra um problema (issue) ou envie uma solicitação de pull (pull request) para colaborar.

## Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo **LICENSE** para obter detalhes.

