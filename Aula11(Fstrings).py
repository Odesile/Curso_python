nome = "Odesilê Moreira"
altura = 1.70
peso = 70
imc = peso/altura**2

#fstring
print(f"{nome} de altura {altura:.2f} pesando {peso}, seu IMC é {imc:.3f}") 

#.format
print("{} de altura {:.2f} pesando {}, seu IMC é {:.3f}".format(nome, altura, peso, imc))

#parâmetros nomeadas
print("{v1} de altura {v2:.2f} pesando {v3}, seu IMC é {v4:.3f}".format(v1=nome, v2=altura, v3=peso, v4=imc))

