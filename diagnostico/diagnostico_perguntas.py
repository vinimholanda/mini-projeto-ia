import random

def faz_perguntas(perguntas, verdadeiros):

    pergunta = random.choice(perguntas)

    #1
    if "fadiga" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("fadiga")
        perguntas.remove("Você tem tido fadiga? [S, N] ")
    #2
    elif "dor de cabeça" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("dor-de-cabeça")
        perguntas.remove("Você tem tido dor de cabeça? [S, N] ")
    #3
    elif "dores no corpo" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("dores-no-corpo")
        perguntas.remove("Você tem tido dores no corpo? [S, N] ")
    #4
    elif "dores de garganta" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("dores-de-garganta")
        perguntas.remove("Você tem tido dores de garganta? [S, N] ")
    #5
    elif "tido tosse" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("tosse")
        perguntas.remove("Você tem tido tosse? [S, N] ")
    #6
    elif "garganta inflamada" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("garganta-inflamada")
        perguntas.remove("Você está com a garganta inflamada? [S, N] ")
    #7
    elif "sentido cansaço" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("cansaço")
        perguntas.remove("Você tem sentido cansaço? [S, N] ")
        #8
    elif "pulsação está" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("pulsação-elevada")
        perguntas.remove("Sua pulsação está elevada? [S, N] ")
    #9
    elif "nível de oxigênio" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("baixo-nível-oxigênio")
        perguntas.remove("Seu nível de oxigênio está baixo? [S, N] ")
    #10
    elif "perda de olfato" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("perda-de-olfato")
        perguntas.remove("Você tem sentido perda de olfato? [S, N] ")
    #11
    elif "perda de paladar" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("perda-de-paladar")
        perguntas.remove("Você tem tido perda de paladar? [S, N] ")
    #12
    elif "coriza" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("coriza")
        perguntas.remove("Você tem tido coriza? [S, N] ")
    #13
    elif "tem espirrado" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("espirro")
        perguntas.remove("Você tem espirrado? [S, N] ")
