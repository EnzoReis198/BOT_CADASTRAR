import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# Dicionário de categorias com palavras-chave
categorias_palavras_chave = {
    "PELICULAS (IPHONE)": ["iphone"],
    "LG": ["lg "],
    "MOTOROLA": ["motorola"],
    "SAMSUNG": ["samsung"],
    "XIAOMI": ["xiaomi"]
}


# Função para categorizar o produto
def categorizar_produto(nome_produto):
    nome_produto = nome_produto.lower()  # Converter o nome do produto para letras minúsculas
    for categoria, palavras in categorias_palavras_chave.items():
        for palavra in palavras:
            if palavra in nome_produto:
                return categoria
    return "OUTROS"  # Retorna uma categoria padrão

navegador = webdriver.Chrome()

navegador.get("https://gestaoclick.com/inicio")
print("Diretório de trabalho atual:", os.getcwd())
df = pd.read_excel("C:/Users/Algo Mais Nova/Desktop/BOT_CADASTRAR/src/PRODUTOS.xlsx")
# df = pd.read_excel("C:/Users/Usuario/Desktop/bot_cadastrar/src/cadastro_produtos_matriz.xlsx")
# print(df)

#efetuar login no site
campo_email = navegador.find_element(By.XPATH, '//*[@id="email"]')
campo_email.send_keys("algomais.com2012@gmail.com")

campo_senha = navegador.find_element(By.XPATH, '//*[@id="senha"]')
campo_senha.send_keys("Algomais2012@")

campo_senha.send_keys(Keys.RETURN)

# Aguarda um pouco
time.sleep(2)

try:
    # click menu
    menu_produtos = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/aside[1]/section/ul/li[2]/a'))
    )
    menu_produtos.click()
    
    time.sleep(2)
    # Localiza e clica na opção "Gerenciar Produtos" dentro do submenu
    gerenciar_produtos = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/aside[1]/section/ul/li[2]/ul/li[1]/a'))
    )
    gerenciar_produtos.click()
    
    time.sleep(2)


    # .columns lista as colunas da tabela
    # print(df.columns) 

    # iloc.[numero] seleciona de acordo a linha solicitada.
    # linha_selecionada = df.iloc[1]
    # nome_produto = linha_selecionada['nome']
    # print(f'Nome do produto: {nome_produto}')

    for index, row in df.iterrows():
        nome_produto = row['nome']
        est_3d = row['est_3d']
        est_ceramica = row['est_ceramica']
        est_privada = row['est_privada']
        est_ceramica_privada = row['est_ceramica_privada']

        # Determina a categoria do produto
        categoria_produto = categorizar_produto(nome_produto)
        print(f'Produto: {nome_produto} | Categoria: {categoria_produto}')
        
        # Clica no botão para adicionar um novo produto
        adicionar_produtos = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="botao-adicionar"]'))
        )
        adicionar_produtos.click()

        # Preenche o formulário de cadastro de produto
        campo_nome = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nome"]')) 
        )
        campo_nome.send_keys(nome_produto)

        #clicar botao gerar codigo interno
        gerar_codigoInterno = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/button'))
        )
        gerar_codigoInterno.click()


        campo_grupo_produto = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="grupo"]')) 
        )
        campo_grupo_produto.send_keys(categoria_produto + Keys.ENTER)


        # Aguarda um pouco antes de adicionar valor produto
        time.sleep(1)
        
        #clicar botao possuir variavel
        possui_variavel = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[1]/div[1]/div[7]/select'))
        )

        possui_variavel.click()

        time.sleep(1)
        
        #clicar botao sim
        variavel_sim = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[1]/div[1]/div[7]/select/option[1]')))

        

        variavel_sim.click()


         # Aguarde até que o botão da aba "ESTOQUE" esteja visível e clique
        aba_estoque = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Estoque/variações"]')) 
        )
        aba_estoque.click()
        


        # Aguarda um pouco
        time.sleep(1)


        #clicar botao valor de peliculas 
        campo_estoque_peliculas = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div/div[11]/label'))
        )
        campo_estoque_peliculas.click()

        # Aguarda um pouco
        time.sleep(1)

                #clicar botao variaveis de pelicula 1
        campo_variaveis_peliculas = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/button[1]'))
        )
        campo_variaveis_peliculas.click()
                #clicar botao variaveis de pelicula 2
        campo_variaveis_peliculas = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/button[1]'))
        )
        campo_variaveis_peliculas.click()
              #clicar botao variaveis de pelicula 3
        campo_variaveis_peliculas = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/button[1]'))
        )
        campo_variaveis_peliculas.click()  





        #adicionar modelo pelicula 3D
        add_modelo_pelicula = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/select'))
        )
        add_modelo_pelicula.click()

                #CLICK 3D
        add_modelo_3D = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/select/option[2]'))
        )
        add_modelo_3D.click()







        #adicionar modelo pelicula CERAMICA
        add_modelo_pelicula = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[3]/select'))
        )
        add_modelo_pelicula.click()

                #CLICK CERAMICA
        add_modelo_ceramica = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[3]/select/option[3]'))
        )
        add_modelo_ceramica.click()







        #adicionar modelo pelicula PRIVADA
        add_modelo_pelicula = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[3]/select'))
        )
        add_modelo_pelicula.click()

                #CLICK PRIVADA
        add_modelo_privada = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[3]/select/option[4]'))
        )
        add_modelo_privada.click()








        #adicionar modelo pelicula CERAMICA PRIVADA
        add_modelo_pelicula = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[3]/select'))
        )
        add_modelo_pelicula.click()

                #CLICK CERAMICA PRIVADA
        add_modelo_ceramica_privada = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[3]/select/option[5]'))
        )
        add_modelo_ceramica_privada.click()






        #clicar botao estoque NORDESTE (3D)
        campo_estoque_3d = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/input'))
        )
        campo_estoque_3d.clear()
        campo_estoque_3d.send_keys((str(est_3d)))




        #clicar botao estoque NORDESTE (CERAMICA)
        campo_estoque_3d = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]/input'))
        )
        campo_estoque_3d.clear()
        campo_estoque_3d.send_keys((str(est_ceramica)))




        #clicar botao estoque NORDESTE (PRIVADA)
        campo_estoque_3d = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]/input'))
        )
        campo_estoque_3d.clear()
        campo_estoque_3d.send_keys((str(est_privada)))


        #clicar botao estoque NORDESTE (CERAMICA PRIVADA)
        campo_estoque_3d = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[4]/input'))
        )
        campo_estoque_3d.clear()
        campo_estoque_3d.send_keys((str(est_ceramica_privada)))





        #ABA DE LOJAS
        aba_lojas = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[1]/ul/li[9]/a'))
        )
        aba_lojas.click()



        #SOMENTE ESTOQUE LOJA NORDESTE
        selecionar_loja_vale = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[1]/div[2]/div[9]/div/div[2]/div/div/div[2]/label'))
        )
        selecionar_loja_vale.click()

        # Aguarda um pouco
        time.sleep(1)


        # CADASTRAR PRODUTO
        cadastrar_produto = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/div/section/form/div[2]/button'))
        )
        cadastrar_produto.click()

        # Aguarda um pouco
        time.sleep(1)

        # Voltar à página de "Adicionar Produto" para cadastrar o próximo produto
        navegador.refresh()

        # Aguarda um pouco
        time.sleep(2)

        
    
    print("Todos os produtos foram cadastrados com sucesso!")
    
    
    



except Exception as e:
    print(f"Erro: {e}")

input("pressione enter para fechar...")