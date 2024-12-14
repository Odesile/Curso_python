#if / elif      / else
#se / se não se / se não

idade = input("Digite aqui sua idade: ")
estado_porta = None
int_idade = int(idade)

if int_idade >= 60:
    print("Infelizmente o senhor é muito velho é perigoso!!")
    estado_porta = "Fechada"
    print(f"Estado da porta: {estado_porta}")

elif int_idade >= 18:
    print("Você é de maior idade, pode passar!!")
    estado_porta = "Aberta"
    print(f"Estado da porta: {estado_porta}")

    vontade_entrar = input("Você quer entrar?? sim ou não? ")

    if vontade_entrar.lower() == 'sim':
        print("Vai lá!! Aproveite!!")
    elif vontade_entrar.lower() == 'não':
        print("Então vai embora e deixa quem quer ir!!!")
    else:
        print("Você não respondeu certo, se manda!!")

else:
    print("Infelizmente você é de menor idade!!")
    estado_porta = "Fechada"
    print(f"Estado da porta: {estado_porta}")