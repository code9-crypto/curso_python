# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'): #Este é o método que inicializa os atributos DA INSTÂNCIA
        #OBS.: dentro do __init__ não precisa ter o return
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod #Método de classe. Acessível apenas por meio de classe
    def create_with_auth(cls, user, password):
        connection = cls()
        #Esses atributos criados(user), são acessíveis apenas dentro do escopo deste método
        connection.user = user 
        connection.passwd = password

        return connection #OBS.: neste @classmethod é necessário sempre ter o return

    @staticmethod #Não muito usado, mas ainda sim existe no python
    def log(msg):
        return 'LOG:', msg




#Classe
c1 = Connection.create_with_auth('luiz', '1234') #aqui não está instanciando a classe, mas sim recebendo o resultado do método da classe
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.passwd)

print(end="\n\n")

#Instancia
c2 = Connection()
c2.set_user('will')
c2.set_password('123456')
print(c2.user)
print(c2.password)

