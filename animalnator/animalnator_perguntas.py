import random

def faz_perguntas(perguntas, verdadeiros):

    pergunta = random.choice(perguntas)

    #1
    if "pelo" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("pelo")
        perguntas.remove("Seu animal tem pelo? [S, N] ")
    #2
    elif "leite" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("leite")
        perguntas.remove("Seu animal dá leite? [S, N] ")
    #3
    elif "tem penas?" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("penas")
        perguntas.remove("Seu animal tem penas? [S, N] ")
    #4
    elif "Seu animal voa?" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("voa")
        perguntas.remove("Seu animal voa? [S, N] ")
    #5
    elif "bota ovos" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("bota-ovos")
        perguntas.remove("Seu animal bota ovos? [S, N] ")
    #6
    elif "come carne" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("come-carne")
        perguntas.remove("Seu animal come carne? [S, N] ")
    #7
    elif "dentes pontiagudos" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("dentes-pontiagudos")
        perguntas.remove("Seu animal tem dentes pontiagudos? [S, N] ")
        #8
    elif "garras" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("garras")
        perguntas.remove("Seu animal tem garras? [S, N] ")
    #9
    elif "olhos frontais" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("olhos-frontais")
        perguntas.remove("Seu animal tem olhos frontais? [S, N] ")
    #10
    elif "casco" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("casco")
        perguntas.remove("Seu animal tem casco [S, N] ")
    #11
    elif "rumina" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("rumina")
        perguntas.remove("Seu animal rumina? [S, N] ")
    #12
    elif "dedos pares" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("dedos-pares")
        perguntas.remove("Seu animal tem dedos pares? [S, N] ")
    #13
    elif "amarelo-tostado" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("amarelo-tostado")
        perguntas.remove("Seu animal tem cor amarelo-tostado? [S, N] ")
    #14
    elif "listras pretas" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("listras-pretas")
        perguntas.remove("Seu animal tem listras pretas? [S, N] ")
    #15
    elif "manchas escuras" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("manchas-escuras")
        perguntas.remove("Seu animal tem manchas escuras? [S, N] ")
    #16
    elif "pernas longas" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("pernas-longas")
        perguntas.remove("Seu animal tem pernas longas? [S, N] ")
    #17
    elif "pescoço comprido" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("pescoço-comprido")
        perguntas.remove("Seu animal tem pescoço comprido? [S, N] ")
    #18
    elif "cor branca" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("branca")
        perguntas.remove("Seu animal tem a cor branca? [S, N] ")
    #19
    elif "preto e branco" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("preto-e-branco")
        perguntas.remove("Seu animal tem a cor preto e branco? [S, N] ")
    #20
    elif "nada" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("nada")
        perguntas.remove("Seu animal nada? [S, N] ")
    #21
    elif "Seu animal é um bom voador?" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("bom-voador")
        perguntas.remove("Seu animal é um bom voador? [S, N] ")
    #22
    elif "corpo arredondado" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("corpo-arredondado")
        perguntas.remove("Seu animal possui um corpo arredondado? [S, N] ")
    #23
    elif "penas densas" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("penas-densas")
        perguntas.remove("Seu animal tem pernas penas densas? [S, N] ")
    #24
    elif "doméstico" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("doméstico")
        perguntas.remove("Seu animal é doméstico? [S, N] ")
    #25
    elif "cauda curta" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("cauda-curta")
        perguntas.remove("Seu animal tem cauda curta? [S, N] ")
    #26
    elif "cor rosa" in pergunta:
        resposta = str(input(f"{pergunta}"))
        if resposta.upper() == "S":
            verdadeiros.append("rosa")
        perguntas.remove("Seu animal tem a cor rosa? [S, N] ")
