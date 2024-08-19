class Conexao:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_pass(self, password):
        self.password = password
        
conex = Conexao()
print(conex.user, conex.password)        
conex.set_user('pedro')
conex.set_pass('12345')
print(conex.user, conex.password)        
