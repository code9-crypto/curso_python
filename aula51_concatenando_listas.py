#CONCATENANDO LISTAS e ESTENDENDO LISTA COM O MÉTODO extend()
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) #este método está pegando a lista 'a' e estendendo para lista 'b'
print(f"lista c {lista_c}")
print(f"lista a extendida {lista_a}")
