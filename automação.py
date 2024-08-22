import pyautogui
import time

# Passo 1: Abrir o navegador/sistema

# isso é uma configuração = a cada comando do pyautogui ele irá dar uma pausa de 0.4 segundos 
pyautogui.PAUSE = 0.4

# abrir o navegador de sua escolha, nesse caso é o Microsoft Edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2)

# entrar no link de algum formulário
pyautogui.write("https://forms.gle/S1iyDfMXk52x8JvG9")
pyautogui.press("enter")
time.sleep(3) # dá uma pausa apenas nesse momento específico

# Passo 2: Fazer login

# clicar no "próximo"
pyautogui.click(x=412, y=242)
time.sleep(0.5)
# selecionar o campo de email
pyautogui.click(x=450, y=403)
# escrever o seu email
pyautogui.write("email@gmail.com")
time.sleep(0.5)
# passar para o próximo campo
pyautogui.press("tab") 
time.sleep(0.5)
pyautogui.write("senha")
# clicar no "próximo"
pyautogui.click(x=505, y=635) 
time.sleep(2.1)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:

    # clicar no campo de código
    pyautogui.click(x=420, y=546)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
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
    if not pd.isna(obs):   # só escrever a informação se o obs for diferente de "NaN", ou seja, se a coluna de obs não estiver vazia
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("tab")

    pyautogui.press("enter") # cadastra o produto (botao enviar)
    time.sleep(0.5)

    # repetir o processo de cadastro até o fim
    # clicar no campo de enviar outra resposta
    pyautogui.click(x=482, y=229)
    time.sleep(0.8)
    # clicar no "próximo"
    pyautogui.click(x=412, y=242)
    time.sleep(0.5)
    # selecionar o campo de email
    pyautogui.click(x=450, y=403)
    time.sleep(0.5)
    pyautogui.write("email@gmail.com")
    time.sleep(0.5)
    pyautogui.press("tab") 
    time.sleep(0.5)
    pyautogui.write("senha")
    pyautogui.click(x=505, y=635)  
    time.sleep(2.1)

