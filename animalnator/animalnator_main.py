import csv
import animalnator_perguntas

def verifica(antecedentes, verdadeiros, alfabeto):

    indice = 0
    julgamento = []
    alfabeto_julgado = []
    antecedentes = [item.replace(" ", "") for item in antecedentes]

    rodar = 0
    while(rodar < 10):
        indice = 0

        # Atribuir valor True ou False a todas as sentenças do alfabeto
        for linha in alfabeto:
            if linha in verdadeiros:
                letra = "True"
                julgamento.append(letra)
            else:
                letra = "False"
                julgamento.append(letra)
        for linha in alfabeto:
            alfabeto_julgado.append(alfabeto[indice] + " = " + julgamento[indice])
            indice = indice + 1
                
       # Atualizar valores
        #R1 
        if "pelo = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("mamífero = False", "mamífero = True") for w in alfabeto_julgado]        
        #R2
        if "leite = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("mamífero = False", "mamífero = True") for w in alfabeto_julgado]  
        #R3
        if "penas = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("ave = False", "ave = True") for w in alfabeto_julgado]
        #R4
        if "voa = True" in alfabeto_julgado and "bota-ovos = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("ave = False", "ave = True") for w in alfabeto_julgado]  
        #R5
        if "mamífero = True" in alfabeto_julgado and "come-carne = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("carnívoro = False", "carnívoro = True") for w in alfabeto_julgado]
        #R6
        if "mamífero = True" in alfabeto_julgado and "dentes-pontiagudos = True" in alfabeto_julgado and "garras = True" in alfabeto_julgado and "olhos- frontais = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("carnívoro = False", "carnívoro = True") for w in alfabeto_julgado]
        #R7
        if "mamífero = True" in alfabeto_julgado and "casco = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("ungulado = False", "ungulado = True") for w in alfabeto_julgado]
        #R8 
        if "mamífero = True" in alfabeto_julgado and "rumina = True" in alfabeto_julgado and "dedos-pares = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("ungulado = False", "ungulado = True") for w in alfabeto_julgado]
        #R9
        if "carnívoro = True" in alfabeto_julgado and "amarelo-tostado = True" in alfabeto_julgado and "manchas-escuras = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("leopardo = False", "leopardo = True") for w in alfabeto_julgado]      
        #R10
        if "carnívoro = True" in alfabeto_julgado and "amarelo-tostado = True" in alfabeto_julgado and "listras-pretas = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("tigre = False", "tigre = True") for w in alfabeto_julgado]
        #R11
        if "ungulado = True" in alfabeto_julgado and "pernas-longas = True" in alfabeto_julgado and "pescoço-comprido = True" in alfabeto_julgado and "amarelo-tostado = True" in alfabeto_julgado and "manchas-escuras = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("girafa = False", "girafa = True") for w in alfabeto_julgado]
        #R12
        if "ungulado = True" in alfabeto_julgado and "branca = True" in alfabeto_julgado and "listras-pretas = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("zebra = False", "zebra = True") for w in alfabeto_julgado]
        #R13
        if "ave = True" in alfabeto_julgado and "pernas-longas = True" in alfabeto_julgado and "pescoço-comprido = True" in alfabeto_julgado and "preto-e-branco = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("avestruz = False", "avestruz = True") for w in alfabeto_julgado]
        #R14
        if "ave = True" in alfabeto_julgado and "voa = False" in alfabeto_julgado and "nada = True" in alfabeto_julgado and "preto-e-branco = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("pinguim = False", "pinguim = True") for w in alfabeto_julgado]
        #R15
        if "ave = True" in alfabeto_julgado and "bom-voador = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("albatroz = False", "albatroz = True") for w in alfabeto_julgado]
        #R16
        if "ave = True" in alfabeto_julgado and "corpo-arrendodado = True" in alfabeto_julgado and "penas-densas = True" in alfabeto_julgado and "voa = False" in alfabeto_julgado and "doméstico = True":
            alfabeto_julgado = [w.replace("galinha = False", "galinha = True") for w in alfabeto_julgado]
        #R17
        if "ave = True" in alfabeto_julgado and "pernas-longas = True" in alfabeto_julgado and "pescoço-comprido = True" in alfabeto_julgado and "cauda-curta = True" in alfabeto_julgado and "rosa = True":
            alfabeto_julgado = [w.replace("flamingo = False", "flamingo = True") for w in alfabeto_julgado]
        rodar = rodar + 1
    
    animais = ["leopardo", "tigre", "girafa", "zebra", "avestruz", "pinguim", "albatroz", "galinha", "flamingo"]

    aux = 0
    # Características
    for linha in verdadeiros:
        if aux == 0:
            print("\nVocê disse que seu animal tem as seguintes carcterísticas: \n")
            aux = aux + 1
        print("- " + linha + ";")
    aux = 0
    aux_2 = 0
    # Dizer animal
    for linha in animais:
        if linha + " = True" in alfabeto_julgado:
            if aux_2 == 0:
                print(f"\nPortando, o animal descrito deve ser: {linha}", end="")
                aux_2 = aux_2 + 1
            else:
                print(f" ou {linha}", end="")
            #break tirar comentário para escolher animal
        else:
            aux = aux + 1
            continue

    if aux == 9:
        print("\nNenhum animal foi encontrado.")

    print("")

if __name__ == "__main__":

    parar = False

    while parar == False:
        print("=== Animalnator ===")
                
        antecedentes = []
        descendentes = []
        antecedentes_e_descendentes = []
        alfabeto = []
        verdadeiros = []
        abc = ["cauda","pelo","mamífero","leite","penas","ave","voa","bota-ovos","come-carne","carnívoro","dentes-pontiagudos","garras","olhos-frontais","casco","ungulado","rumina","dedos-pares","amarelo-tostado","manchas-escuras","leopardo","listras-pretas","tigre","pernas-longas","pescoço-comprido","girafa","branca","zebra","preto-e-branco","avestruz","não-voa","nada","pinguim","bom-voador","albatroz","corpo-arredondado","penas-densas","doméstico","galinha","cauda-curta","rosa","flamingo", "pernas-densas"]
        perguntas = ["Seu animal tem pelo? [S, N] ", 
                "Seu animal dá leite? [S, N] ", 
                "Seu animal tem penas? [S, N] ", 
                "Seu animal voa? [S, N] ", 
                "Seu animal bota ovos? [S, N] ", 
                "Seu animal come carne? [S, N] ", 
                "Seu animal tem dentes pontiagudos? [S, N] ", 
                "Seu animal tem garras? [S, N] ", 
                "Seu animal tem olhos frontais? [S, N] ", 
                "Seu animal tem casco [S, N] ", 
                "Seu animal rumina? [S, N] ", 
                "Seu animal tem dedos pares? [S, N] ", 
                "Seu animal tem cor amarelo-tostado? [S, N] ",
                "Seu animal tem listras pretas? [S, N] ",
                "Seu animal tem manchas escuras? [S, N] ",
                "Seu animal tem pernas longas? [S, N] ",
                "Seu animal tem pescoço comprido? [S, N] ",
                "Seu animal tem a cor branca? [S, N] ",
                "Seu animal tem a cor preto e branco? [S, N] ",
                "Seu animal nada? [S, N] ",
                "Seu animal é um bom voador? [S, N] ",
                "Seu animal possui um corpo arredondado? [S, N] ",
                "Seu animal tem pernas penas densas? [S, N] ",
                "Seu animal é doméstico? [S, N] ",
                "Seu animal tem cauda curta? [S, N] ",
                "Seu animal tem a cor rosa? [S, N] "]

        print("\nSeus dados:\n")
        with open("./animalnator/regras_animalnator.csv", "r") as base:
            ler_base = csv.reader(base)
            next(ler_base)

            for linha in ler_base:
                antecedentes.append(linha[0])
                descendentes.append(linha[1])
                antecedentes_e_descendentes.append(linha[0]+">"+linha[1])

                print(linha)

            print("")
        parar = True

    # Cria alfabeto
    for linha in abc:
        if linha in abc and linha not in alfabeto:
            alfabeto.append(linha)
        else:
            continue
    # Faz as perguntas
    x = 0
    while (x < 26):

        animalnator_perguntas.faz_perguntas(perguntas, verdadeiros)
        x = x + 1

    # Julga aqui
    verifica(antecedentes, verdadeiros, alfabeto)