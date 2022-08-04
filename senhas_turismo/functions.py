from ctypes.wintypes import PWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .cad_usuario import cadastrarUsuario
from .cad_compras import cadastrarViagemCompra
from .cad_compras_e_turismo import cadastrarViagemTurismoECompras
from senhas_turismo.cad_pico_caledonia import CadastrarViagemPicoDaCaledonia

def inflogin():
    print(''''
    Bem vindo
    
    ''')
    email=input('Email: ')
    pw=input('Senha: ')
    return email, pw


def login(driver, email, pw):
    # logando no site
    driver=webdriver.Chrome()
    driver.get("http://localhost:8000/login/")
    username = driver.find_element(By.NAME, "username")
    username.send_keys(email)
    pwpw = driver.find_element(By.NAME, "password")
    pwpw.send_keys(pw)
    btn = driver.find_element(By.TAG_NAME, "button")
    btn.click()
    return driver

def logout(driver):
    driver=webdriver.Chrome()
    driver.get("http://localhost:8000/contas/sair/")

def run(cmd, email, pw):
    driver=None
    is_authenticated=False
    
    opcoes={
        'user': cadastrarUsuario,
        'tc': cadastrarViagemTurismoECompras,
        'c': cadastrarViagemCompra,
        'pc': CadastrarViagemPicoDaCaledonia,    
    }

    #cambiarra
    cmds=[]
    for i in opcoes:
        cmds.append(i)
    print(cmds)
    while cmd!='exit':
        try:
            if cmd in cmds:
                
                if not is_authenticated:
                    if cmd == "user":
                        cadastrarUsuario(driver)
                    else:                        
                        driver = login(driver, email, pw)
                        is_authenticated=True
                elif  cmd == "user":
                    logout(driver)

                opcoes[cmd](driver)
            else:
                print('Este comando não existe. Tente outro.')
        except Exception as E:
            print('Error:', E)
        print('- O que deseja fazer?')
        cmd=input('>> ')
# if __name__=='__main__':
#     print('teste')