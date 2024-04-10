import datetime as dt

class Pessoa:
    def __init__(self, nome, nascimento, apelido):
        self.nome = nome
        self.nascimento = dt.datetime.strptime(nascimento, "%d-%m-%Y")
        self.apelido = apelido
        self.idade = self.calcularIdade()
        self.sis = self.sistema()

    def calcularIdade(self):
        hoje = dt.datetime.now()
        diferenca = hoje - self.nascimento
        diferenca = diferenca.days // 365
        return diferenca
    
    def sistema(self):
        sist = dt.datetime.now().hour
        if sist >= 5 and sist <= 11:
            return print("Bom Dia!")
        elif sist >= 12 and sist <= 17:
            return print("Boa Tarde!")
        elif sist >= 18 and sist <= 23:
            return print("Boa Noite!")
        elif sist >= 0 and sist <= 5:
            return print("Vai Dormir!")
        
    def saudacao(self):    
        return f'Ola, me chamo {self.nome},\n mas meu apelido é {self.apelido}, e tenho {self.idade} anos.'

class Aluno(Pessoa):
    

class Professor(Aluno):


class Funcionario(Pessoa):
