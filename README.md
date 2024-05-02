# Generate Qr 

:heavy_check_mark: Um projeto simples, projetado para gerar códigos QRs possuindo uma UI básica.

## Instalando as dependências
Para o projeto funcionar, precisamos instalar todas as dependências nescessárias, como o ele é pequeno, ele possuí poucas. Instalaremos as dependências utilizando o `venv` para que elas não atrapalhem ou sejam atrapalhadas pelo funcionamento de outros projetos. Utilizamos o seguinte comando para criar um ambiente-virtual:
> [!NOTE]
> Estou utilizando o Git Bash como terminal para executar os comandos.
```
$ python3 -m venv .venv # Mac ou Linux
# ou
$ python -m venv .venv # Windows
```
Precisamos ativar ele:
```
$ source .venv/bin/activate # Mac ou Linux
# ou
$ source .venv/Script/activate # Windows
```
Após o processo de criação e ativação do `venv`. Iremos realizar a instalação dos arquivos que estão no `requirements.txt`:
```
pip install -r requirements.txt
```
Pronto, a etapa de instalação foi concluída. :grin::grin:

## Iniciando o projeto
Para iniciar o projeto, basta rodar o seguinte comando no terminal:
```
$ python3 app/view.py # Mac ou Linux
# ou
$ python app/view.py # Windows
```

> [!IMPORTANT]
> As imagens QR Codes criadas são `.png` e armazenadas na pasta :file_folder:`media/qrs/` 
