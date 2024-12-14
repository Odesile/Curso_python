'''
input() -> função que solicita dados do usuário
'''

nome = input("Qual o seu nome?: ")
idade = input("Qual a sua idade?: ")
altura = input("Qual a sua altura?: ")

int_idade = int(idade)
float_altura = float(altura)

print(f"{nome} de {int_idade} anos de idade, e de altura {float_altura:.2f}")