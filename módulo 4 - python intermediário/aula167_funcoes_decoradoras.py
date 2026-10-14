# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao #OBS.: esta notação troca o nome desta função para a função interna desta
# E para que isso funcione, a função criadora só pode receber como parâmetro a função
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


#COM A NOTAÇÃO @criar_funcao eu não preciso mais desta lógica, porque isso já simplifica
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('lista')
# print(invertida)

#AGORA FICA SIMPLESMENTE DESTE JEITO
invertida = inverte_string('123')
print(invertida)
