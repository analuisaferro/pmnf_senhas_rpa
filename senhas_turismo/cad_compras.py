from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

def cadastrarViagemCompra(driver):
    #cadastro gp turismo e compras
    driver.get("http://localhost:8000/cad_viagem/c/compras")
    nomeRes = driver.find_element(By.ID, "id_responsavel_viagem")
    nomeRes.send_keys("Cristiane Catarina Moura")
    contatoRes = driver.find_element(By.ID, "id_contato_responsavel")
    contatoRes.send_keys("67995671982")
    estado = driver.find_element(By.ID, "id_estado")
    estado.send_keys("S")
    cidade = driver.find_element(By.ID, "id_cidade")
    cidade.send_keys("G")
    dtchegada = driver.find_element(By.ID, "dt_chegada")
    dtchegada.send_keys("27102022")
    dtsaida = driver.find_element(By.ID, "dt_saida")
    dtsaida.send_keys("29102022")
    emptrans = driver.find_element(By.ID, "id_empresa_transporte")
    emptrans.send_keys("2002")
    cadEmp = driver.find_element(By.ID, "id_cadastur_empresa_transporte")
    cadEmp.send_keys("856471254")
    cnpj = driver.find_element(By.ID, "cnpj")
    cnpj.send_keys("04981750000142")
    quantps = driver.find_element(By.ID, "id_quant_passageiros")
    quantps.send_keys("26")
    tipovei = driver.find_element(By.ID, "id_tipo_veiculo")
    tipovei.send_keys("v")
    btnCad = driver.find_element(By.ID, "submit")
    btnCad.click()
    pyautogui.hotkey('enter')
    # driver.close()