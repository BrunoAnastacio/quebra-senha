
"""
-- O OBJETIVO EH MOSTRAR COMO SERIA FACIL QUEBRAR UMA SENHA PURAMENTE NUMERICA

-- O CODIGO PEDE AO USUARIO QUE INFORME UMA SENHA E ENTAO ELE TENTA, REPETIDAMENTE, ~ADIVINHAR~ QUAL EH A SENHA INFORMADA.

-- EH IMPRRSSIONANTE A RAPIDEZ QUE UM COMPUTADOR PODE QUEBRAR UMA SENHA DE SEIS DIGITOS (O TIPO UTILIZADO NOS BANCOS BRASILEIROS). EH POR ISSO QUE OS BANCOS SEMPRE UTILIZAM FORMAS ASSOCIADAS DE VERIFICACAO, TIPO BIOMETRIA, CHAVE TOKEN E ETC.

-- EH POR ISSO TBM QUE OUTROS SISTEMAS EXIGEM USO DR CARACTERES DIVERSOS NA COMPOSIÇÃO DE SENHAS.

-- OBVIO QUE QUEBRAR SENHAS DE BANCO ENVOLVE MUITO MAIS QUE ISSO, NÉ? ESTA É APENAS UMA BRINCADEIRA PARA MOSTRAR O PODER DE PROCESSAMENTO DE UM COMPUTADOR. HOLD ON, HACKUDAO!

"""

#importando função randint que vai gerar o numero aleatório repetidamente até adivinhar a senha
from random import randint 
#importando a função time, que vai nos ajudar a medir quanto tempo demoramos até quebrar a senha
from time import time

cont = 0 #variavel onde vamos contar quantas tentativas fizemos
senha = -1 #variavel onde vamos salvar a senha que o usuario vai informar
qSenha = -1 #variavel que vai armazenar a senha aleatória que o codigo vai tentar usar pra quebrar a senha do usuario


inicioExecucao = time() #marcando o inicio da execucao do programa

#while deixa a execução em loop até o usuario informar a senha dele
while senha == -1:
    senha = int(input("Digite senha de seis digitos\n")) #usuario informa senha
    if senha >-1 and senha < 1000000: #verifica se a senha tem seis digitos
        #while faz a execucao ficar em loop até o codigo gerar uma senha igual a do usuario
        while senha != qSenha: 
            qSenha = randint(0,999999) #essa linha gera uma "senha" aleatória
            cont=cont+1 #aqui contamos quantas vezes o sistema tentou gerar uma senha até a execução
        #mostramos ao usuario a senha que ele digitou
        print ("\nSenha digitada: " + str(senha)) 
        #mostrams ao usuario quantas vezes insistimos até conseguir gerar a senha certa
        print ("\nTentativas ate quebrar senha: " + str(cont))
        fimExecucao = time() #marcamos o fim da execução do programa
        tempoExecucao = fimExecucao - inicioExecucao #calculamos o tempo de execucão do programa
        #mostramos ao usuario quantos segundos levamos até invadir a conta dele
        print ("\nTempo de tentativa, em segundos: " + str(tempoExecucao))
        print ("\nTentativas por segundo: " + str(cont/tempoExecucao))
    #caso o usuario não informe uma senha com seis digitos    
    else:
        print ("Rode o programa novamente, digitando senha de seis digitos")


