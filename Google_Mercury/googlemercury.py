import csv
from ctypes.wintypes import PWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
screenWidth, screenHeight = pyautogui.size()

driver=webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fcontacts.google.com%2Fu%2F1%2F%3Fhl%3Den&followup=https%3A%2F%2Fcontacts.google.com%2Fu%2F1%2F%3Fhl%3Den&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH ,"//span[contains(text(), 'Create contact')]"))
    )
except:
    pass

# email = driver.find_element(By.ID, "identifierId")
# email.send_keys("teste.umtestezinho@gmail.com")
# btnLogin = driver.find_element(By.XPATH ,"//span[contains(text(), 'Next')]") #ASSIM
# btnLogin.click()
# try:
#     element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "selectionc2"))
#     )
# except:
#     pass
# # senha = driver.find_element(By.XPATH,"//input[contains(text(), 'Enter your password')]")  <--- NAO PRECISAA
# pyautogui.write('teste*12345678', interval=0.1)
# sendd = driver.find_element(By.XPATH ,"//span[contains(text(), 'Next')]")
# sendd.click()
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH ,"//span[contains(text(), 'Create contact')]"))
    )
except:
    pass
ctt = driver.find_element(By.XPATH ,"//span[contains(text(), 'Create contact')]")
ctt.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH ,"//span[contains(text(), 'Create a contact')]"))
    )
except:
    pass

createCtt = driver.find_element(By.XPATH ,"//span[contains(text(), 'Create a contact')]")
createCtt.click()

arquivo = './Google_Mercury/alunos_cevest.csv'

def cadastrar_contato(l):
    nome=l[0]
    numero=l[-1]
    # teste*12345678 <--- senha


def lerArquivo(arquivo):
    arquivoAberto = open(arquivo, 'r')
    return csv.reader(arquivoAberto, delimiter=',')

dados=lerArquivo(arquivo)
for l in dados:
    cadastrar_contato(l)

