import sqlite3

def conectar_banco():
  global conexao, cursor
  conexao = sqlite3.connect('jogo_sql.db')
  cursor = conexao.cursor()
  return conexao, cursor

def commit_banco():
  conexao.commit()

def fechar_conexao():
  conexao.close()

