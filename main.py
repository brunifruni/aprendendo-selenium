from selenium import webdriver
import time

#para abrir o navegador
navegador = webdriver.Chrome()

#acessar o site
navegador.get('https://www.hashtagtreinamentos.com/')

#maximizar a tela do navegador
navegador.maximize_window()

#selecionar um elemento na tela
#botao_verde = navegador.find_element("class name", "botao-verde")

#clicar em um elemento
#botao_verde.click()

#encontrar varios elementos
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

#abrir nova aba em branco
navegador.execute_script("window.open('');")
time.sleep(1)
#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

#navegar para um site diferente

navegador.get("https://hashtagtreinamentos.com/curso-python")

#escrever em um campo
#com variavel
campo_nome = navegador.find_element("id", "firstname")
campo_nome.send_keys("Lira")
#sem variavel
navegador.find_element("id", "email").send_keys("email@teste.com.br")

navegador.find_element("id", "phone").send_keys("51 9984645248")

botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

#dar scroll / colocar um elemento na tela
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",botao_quero_clicar)

#opcoes para o selenium esperar as paginas carregarem

#opcao 1 - espera manual - direta
#time.sleep(3) #espera 3 segundos para clicar no botao

#opcao 2 - espera dinamica
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
#se ele nao encontrar o botao em 10 seg ele vai para a proxima linha de codigo
espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()

time.sleep(10)