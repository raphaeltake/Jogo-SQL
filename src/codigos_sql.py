def verificar_jogo_existente():
  return "SELECT name FROM sqlite_master WHERE name='jogo'"

def apagar_jogo():
  return "DROP TABLE jogo"

#Create table genérica, apenas para testar
def criacao_tabela_jogo():
  return "CREATE TABLE jogo (ID INT PRIMARY KEY, Nome VARCHAR(100), Email VARCHAR(100), Idade INT);"