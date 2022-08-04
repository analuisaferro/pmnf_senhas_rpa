import senhas_turismo.functions as fc
import os
os.system('cls')


email, pw=fc.inflogin()

print('''

Comandos:
    user - Realiza um cadastro de usuário
    tc - Realiza um cadastro de senha p/ Grupo p/ Turismo e Compras
    c - Realiza um cadastro de senha p/ Grupo Exclusivamente p/ Compras
    pc - Realiza um cadastro de senha p/ o Pico do Caledonia

    
    - O que você desejar fazer?
''')


if __name__=='__main__':
    cmd=input()
    fc.run(cmd, email, pw)