
import os
import sys
from src import conexao_banco as cb
from src import codigos_sql as cs

def apagar_jogo():
    cursor.execute(cs.apagar_jogo())
    menu_principal()

#Continua o jogo, caso o jogador tenha um jogo ativo
def continuar_jogo():
    print("continuar jogo")

#Salva o jogo, fecha a conexão com o db e fecha o jogo
def fechar_jogo():
    salvar_jogo()
    cb.fechar_conexao()
    sys.exit()

#Limpa o console (deixa o console menos poluído)
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Menu principal do jogo
def menu_principal():
    limpar_console()
    #Menu para o jogador que já tenha um jogo criado
    opcoes_menu_jogo_existente = """
[1] Continuar jogo
[2] Novo jogo
[3] Sair do jogo
[0] Apagar jogo
    """

    #Menu para o jogador que está jogando pela primeira vez ou perdeu o último jogo
    opcoes_menu_apenas_novo_jogo = """
[1] Novo jogo
[2] Sair do jogo
    """

    #Verifica se o jogar tem um jogo ativo
    if verifica_jogo_existente():
        print(opcoes_menu_jogo_existente)
        opcoes = {"1": continuar_jogo, "2": novo_jogo, "3": fechar_jogo, "0": apagar_jogo}
    else:
        print(opcoes_menu_apenas_novo_jogo)
        opcoes = {"1": novo_jogo, "2": fechar_jogo}

    opcao_escolhida = input('Selecione uma opção: ')

    #Verifica se foi digitado uma opção existente no contexto do jogador
    if opcao_escolhida not in opcoes:
        input('Essa não é um opção! aperte qualque tecla para tentar novamente.')
        menu_principal()
        return
    opcoes[opcao_escolhida]()

#Cria um novo jogo
def novo_jogo():
    #Tenta criar uma tabela de jogo
    try:
        cursor.execute(cs.criacao_tabela_jogo())
        
    #Caso já tenha uma tabela de jogo criada, será perguntada ao jogador se ele realmente deseja criar um novo jogo. Caso "sim", a tabela "jogo" será apagada.
    except:
        opcao = input("Atenção! Isso irá apagar seu jogo anterior. Deseja continuar [s/n]? ")
        if opcao.lower() == 's':
            cursor.execute(cs.apagar_jogo())
            cursor.execute(cs.criacao_tabela_jogo())
            print("tabela jogo criada")
    menu_principal()

#Usado para salvar o jogo
def salvar_jogo():
    cb.commit_banco()

#Verifica se há algum jogo ativo
def verifica_jogo_existente():
    global cursor
    res = cursor.execute(cs.verificar_jogo_existente())
    return res.fetchone() is not None

#Função Main do jogo.
def main(con):
    global conexao, cursor
    conexao, cursor = con
    limpar_console()
    menu_principal()

