import datetime as dt
dia = dt.datetime.now()
print(dia)
nasc = dt.datetime(day=20, month=7, year=2000)
print(nasc)
calcidade = dia - nasc
idade = calcidade.days//365
print(idade)