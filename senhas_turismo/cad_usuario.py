from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def cadastrarUsuario(driver):
    btnlogin_cad = driver.find_element(By.ID, "cad_usuario")
    btnlogin_cad.click()

    usuario = driver.find_element(By.ID, "id_nome")
    usuario.send_keys("Gabriela Carrasco Farias")
    cpf = driver.find_element(By.ID, "id_cpf")
    cpf.send_keys("92637569026")
    email = driver.find_element(By.ID, "id_email")
    email.send_keys("rebecaadriana@kaynak.com.br")
    celular = driver.find_element(By.ID, "id_celular")
    celular.send_keys("79992749723")
    telefone = driver.find_element(By.ID, "id_telefone")
    telefone.send_keys("7929974838")
    estado = driver.find_element(By.ID, "id_estado")
    estado.send_keys("S")
    cidade = driver.find_element(By.ID, "id_cidade")
    cidade.send_keys("G")
    senha = driver.find_element(By.ID, "id_senha")
    senha.send_keys("wnnUFfeqAl")
    senhaconf = driver.find_element(By.ID, "id_senha_confirma")
    senhaconf.send_keys("wnnUFfeqAl")
    btn_cad = driver.find_element(By.TAG_NAME, "button")
