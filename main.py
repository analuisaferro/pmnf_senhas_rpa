import senhas_turismo.functions as fc

print('Bem vindo')
print('''

Comandos:
    caduser - Realiza um cadastro de usuário
    cadtc - Realiza um cadastro de senha p/ Grupo p/ Turismo e Compras
    cadc - Realiza um cadastro de senha p/ Grupo Exclusivamente p/ Compras
    cadpc - Realiza um cadastro de senha p/ o Pico do Caledonia

    
    - O que você desejar fazer?
''')

cmd=input()

fc.run(cmd)