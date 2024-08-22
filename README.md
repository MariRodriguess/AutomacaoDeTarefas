# Automação de Cadastro de Produtos

Este é um código de automação em Python, desenvolvido para facilitar o cadastro de produtos em um formulário online, como um Google Formulário. O script utiliza a biblioteca `pyautogui` para simular interações com a interface do usuário, como cliques e digitação, e lê os dados dos produtos a partir de um arquivo CSV.

## Funcionalidades

- **Automação de Tarefas:** O código foi projetado para abrir um navegador, acessar um formulário do google e preencher automaticamente os campos com os dados do produto extraídos de um arquivo CSV.
- **Flexibilidade:** O script pode ser adaptado para diferentes formulários ou sistemas, com base nas necessidades específicas do usuário. 
- **Repetição de Processos:** Permite a repetição do cadastro de vários produtos, automatizando completamente o processo.

## Bibliotecas Utilizadas

- **`pyautogui:`** Biblioteca principal utilizada para a automação da interface gráfica do usuário (GUI). Com ela, é possível simular cliques do mouse, digitação, pressionamento de teclas, entre outras ações.
- **`pandas:`** Utilizada para manipulação e leitura do arquivo CSV que contém os dados dos produtos.

## Principais Funções da Biblioteca `pyautogui`

- **`pyautogui.click(x, y):`** Clica com o mouse nas coordenadas especificadas.
- **`pyautogui.position():`** Retorna a posição atual do cursor do mouse na tela.
- **`pyautogui.write(texto):`** Digita o texto especificado.
- **`pyautogui.press(tecla):`** Pressiona uma tecla específica.
- **`pyautogui.hotkey(teclas):`** Combina e pressiona múltiplas teclas simultaneamente, como `Ctrl + C`.
- **`pyautogui.scroll(val):`** Rola a tela para cima ou para baixo.
## Como Rodar o Código

1. **Instale as Bibliotecas Necessárias:**
   ```bash
   pip install pyautogui pandas
   ```

2. **Configure os Clipes e Posições:**
   - Execute o código `automacao.py` e verifique se os cliques e posições na tela correspondem ao layout do seu monitor. Caso contrário, utilize a função `pyautogui.position()` para ajustar as coordenadas dos cliques.

3. **Rode o Script:**
   - Após a configuração, rode o script para automatizar o cadastro dos produtos.

## Adaptações

Este código pode ser facilmente ajustado para automatizar outras tarefas repetitivas no computador, como o preenchimento de diferentes formulários, interações em sistemas desktop ou qualquer processo que exija a simulação de ações de teclado e mouse. Além disso, ele pode ser adaptado para lidar com diferentes tipos de arquivos de dados.

