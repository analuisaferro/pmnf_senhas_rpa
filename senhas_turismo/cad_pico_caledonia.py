from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

#cadastro gp turismo e compras
def CadastrarViagemPicoDaCaledonia(driver):

    gppc = driver.find_element(By.ID, "caledonia")
    gppc.click()
    nomeRes = driver.find_element(By.ID, "id_responsavel_viagem")
    nomeRes.send_keys("Cristiane Catarina Moura")
    contatoRes = driver.find_element(By.ID, "id_contato_responsavel")
    contatoRes.send_keys("67995671982")
    estado = driver.find_element(By.ID, "id_estado")
    estado.send_keys("S")
    cidade = driver.find_element(By.ID, "id_cidade")
    cidade.send_keys("G")
    dtvisi = driver.find_element(By.ID, "dt_chegada")
    dtvisi.send_keys("27102022")
    emptrans = driver.find_element(By.ID, "id_empresa_transporte")
    emptrans.send_keys("2002")
    cadEmp = driver.find_element(By.ID, "id_cadastur_empresa_transporte")
    cadEmp.send_keys("856471254")
    cnpj = driver.find_element(By.ID, "cnpj")
    cnpj.send_keys("04981750000142")
    quantps = driver.find_element(By.ID, "id_quant_passageiros")
    quantps.send_keys("34")
    tipovei = driver.find_element(By.ID, "id_tipo_veiculo")
    tipovei.send_keys("o")
    nomeGuia = driver.find_element(By.NAME, "nome_guia")
    nomeGuia.send_keys("Yuri Tomás Fábio Santos")
    cadGuia = driver.find_element(By.NAME, "cadastur_guia")
    cadGuia.send_keys("856985412")
    contatoGuiaCel = driver.find_element(By.ID, "celular")
    contatoGuiaCel.send_keys("67994773753")
    contatoGuiaTel = driver.find_element(By.ID, "telefone")
    contatoGuiaTel.send_keys("6729431270")
    btnCad = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    btnCad.click()
    pyautogui.hotkey('enter')
# driver.close()
