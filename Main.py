import sqlite3
import sys
import os

#Continua o jogo, caso o jogador tenha um jogo ativo
def continuar_jogo():
    print("continuar jogo")

#Salva o jogo, fecha a conexão com o db e fecha o jogo
def fechar_jogo():
    salvar_jogo()
    conexao.close()
    sys.exit()

#Limpa o console (deixa o console menos poluído)
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Menu principal do jogo
def menu_jogo():
    #Menu para o jogador que já tenha um jogo criado
    opcoes_menu_jogo_existente = """
[1] Continuar jogo
[2] Novo jogo
[3] Sair do jogo
    """

    #Menu para o jogador que está jogando pela primeira vez ou perdeu o último jogo
    opcoes_menu_apenas_novo_jogo = """
[1] Novo jogo
[2] Sair do jogo
    """

    #Verifica se o jogar tem um jogo ativo
    if verifica_jogo_existente():
        print(opcoes_menu_jogo_existente)
        opcoes = {"1": continuar_jogo, "2": novo_jogo, "3": fechar_jogo}
    else:
        print(opcoes_menu_apenas_novo_jogo)
        opcoes = {"1": novo_jogo, "2": fechar_jogo}

    opcao_escolhida = input('Selecione uma opção: ')

    #Verifica se foi digitado uma opção existente no contexto do jogador
    if opcao_escolhida not in opcoes:
        limpar_console()
        print('Essa não é um opção')
        menu_jogo()
        return
    opcoes[opcao_escolhida]()

#Cria um novo jogo
def novo_jogo():
    #Create table genérica, apenas para testar
    criacao_tabela_jogo = "CREATE TABLE jogo (ID INT PRIMARY KEY, Nome VARCHAR(100), Email VARCHAR(100), Idade INT);"

    #Tenta criar uma tabela de jogo
    try:
        cursor.execute(criacao_tabela_jogo)
        
    #Caso já tenha uma tabela de jogo criada, será perguntada ao jogador se ele realmente deseja criar um novo jogo. Caso "sim", a tabela "jogo" será apagada.
    except:
        opcao = input("Atenção! Isso irá apagar seu jogo anterior. Deseja continuar [s/n]? ")
        if opcao.lower() == 's':
            cursor.execute("DROP TABLE jogo")
            cursor.execute(criacao_tabela_jogo)

    print("tabela jogo criada")
    menu_jogo()

#Usado para salvar o jogo
def salvar_jogo():
    conexao.commit()

#Verifica se há algum jogo ativo
def verifica_jogo_existente():
    global cursor
    res = cursor.execute("SELECT name FROM sqlite_master WHERE name='jogo'")
    return res.fetchone() is not None

#Função Main do jogo.
def main():
    global conexao
    conexao = sqlite3.connect('jogo_sql.db')
    global cursor
    cursor = conexao.cursor()
    limpar_console()
    menu_jogo()

main()