# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1 # 1 segundo de pausa após cada comando do pyautogui

# abrir o navegador (qualquer navegador)
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")   
time.sleep(3) # esperar 3 segundos

# entrar no link    
pyautogui.click(x=239, y=59) # clicar na barra de endereços do navegador
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #esperar 3 segundos


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=735, y=363) # clicar no campo de email

pyautogui.write("pythonimpressionador@gmail.com") # escrever o seu email
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha") # escrever a sua senha
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter") # apertar o botão entrar
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto e repetir o processo até o fim
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=729, y=244)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # se tiver algo na observação
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

