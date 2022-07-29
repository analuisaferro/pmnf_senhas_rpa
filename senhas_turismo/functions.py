from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .cad_usuario import cadastrarUsuario
from .cad_compras import cadastrarViagemCompra
from .cad_compras_e_turismo import cadastrarViagemTurismoECompras
from senhas_turismo.cad_pico_caledonia import CadastrarViagemPicoDaCaledonia

def login(driver):
    # logando no site
    driver=webdriver.Chrome()
    driver.get("http://localhost:8000/login/")
    username = driver.find_element(By.NAME, "username")
    username.send_keys("analuisaferro@gmail.com")
    pw = driver.find_element(By.NAME, "password")
    pw.send_keys("12345678")
    btn = driver.find_element(By.TAG_NAME, "button")
    btn.click()
    
def run(cmd):
    driver=None
    is_authenticated=False
    
    opcoes={
        'caduser': cadastrarUsuario,
        't': cadastrarViagemTurismoECompras,
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
                    login(driver)
                    is_authenticated=True
                opcoes[cmd](driver)
            else:
                print('Este comando não existe. Tente outro.')
        except Exception as E:
            print('Error:', E)
        print('- O que deseja fazer?')
        cmd=input('>> ')
