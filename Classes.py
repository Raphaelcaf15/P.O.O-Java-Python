import datetime as dt
class Pessoa:
    def __init__(self, nasc):
        self.nasc = dt.datetime.strptime(nasc, "%d-%m-%Y")
        self.idade = self.CalcIdad()

    def CalcIdad(self):
        hoje = dt.datetime.now()
        calc = hoje - self.nasc
        calc = calc.days // 365
        return calc
    def Saudacao(self):
        return f"Olá eu tenho {self.idade} anos"
    
class Aluno