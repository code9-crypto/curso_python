import os as sistema
import time as tempo

nome = "william"

#locals() e globals() -> tem um comportamento equivalentes, pois exibem chaves e valores do módulo em questão
#namespace -> é o nome que define o módulo. Também é por ele que pode acessar as de mais funções
#dir() -> basicamente mostra apenas as chaves do namespace
#vars() -> basicamente mostra chave e valor
#__name__ -> é o nome do módulo em que os comandos estão sendo executados
#OBS.: por padrão seu nome é __main__

print("Locals -> ", locals(), end="\n\n")
print("Globals -> ", globals(),  end="\n\n")
print("Nome do módulo -> ", __name__, end="\n\n")
print("Nome do arquivo -> ", __file__, end="\n\n")
print("Chaves nativas dos builtins(código nativo) -> ", dir(__builtins__), end="\n\n")
print("Chaves e valores nativos builtins(código nativo) -> ", vars(__builtins__))

# Mostrando as chaves da classe time
print("Chaves da classe time -> ", dir(tempo))

# Mostrando as chaves da classe os
print("Chaves da classe OS ->", dir(sistema))

#*****************************************************************************************************************
#Busca por nomes acontece da seguinte maneira
#CERTO: local -> enclosing -> global -> built-in -> NameError(se não encontrar, será lançado este erro)
#ERRADO: built-in -> global -> enclosing -> local