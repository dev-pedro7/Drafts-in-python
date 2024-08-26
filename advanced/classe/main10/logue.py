# Abstração
# Heranca - é um
class Log:
    def log(self,msg):
        raise NotImplementedError('implemente o metodo log')

class LogFileMixin(Log):
    def log(self,msg):
        print(msg)

if __name__ == '__main__':
    l = LogFileMixin()
    l.log('any')