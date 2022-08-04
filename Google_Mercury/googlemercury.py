import csv
from ctypes.wintypes import PWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fcontacts.google.com%2Fu%2F1%2F%3Fhl%3Den&followup=https%3A%2F%2Fcontacts.google.com%2Fu%2F1%2F%3Fhl%3Den&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

arquivo = './Google_Mercury/alunos_cevest.csv'
# são 30 virgulas ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
def cadastrar_contato(l):
    nome=l[0]
    numero=l[-1]


def lerArquivo(arquivo):
    arquivoAberto = open(arquivo, 'r')
    return csv.reader(arquivoAberto, delimiter=',')

dados=lerArquivo(arquivo)
for l in dados:
    cadastrar_contato(l)

