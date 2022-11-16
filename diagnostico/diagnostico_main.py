import csv
import diagnostico_perguntas

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
        if "fadiga = True" in alfabeto_julgado and "dor-de-cabeça = True" in alfabeto_julgado and "dores-no-corpo = True" in alfabeto_julgado and "dores-de-garganta = True" in alfabeto_julgado and "tosse = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("covid19(FC = 0.80) = False", "covid19(FC = 0.80) = True") for w in alfabeto_julgado]
        #R2
        if "dor-de-cabeça = True" in alfabeto_julgado and "garganta-inflamada = True" in alfabeto_julgado and "tosse = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("gripe(FC = 0.90) = False", "gripe(FC = 0.90) = True") for w in alfabeto_julgado]        
        #R3
        if "cansaço = True" in alfabeto_julgado and "dor-de-cabeça = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("mononucleose infecciosa(FC = 0.95) = False", "mononucleose infecciosa(FC = 0.95) = True") for w in alfabeto_julgado]
        #R4
        if "cansaço = True" in alfabeto_julgado and "garganta-inflamada = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("amigdalite(FC = 0.90) = False", "amigdalite(FC = 0.90) = True") for w in alfabeto_julgado]
        #R5 
        if "cansaço = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("estresse(FC = 0.70) = False", "estresse(FC = 0.70) = True") for w in alfabeto_julgado]        
        #R6
        if "fadiga = True" in alfabeto_julgado and "dor-de-cabeça = True" in alfabeto_julgado and "pulsação-evedada = True" in alfabeto_julgado and "baixo-nível-oxigênio = True" in alfabeto_julgado and "perda-de-ofalto = True" in alfabeto_julgado and "perda-de-paladar = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("covid19(FC = 0.90) = False", "covid19(FC = 0.90) = True") for w in alfabeto_julgado]
        #R7
        if "coriza = True" in alfabeto_julgado and "espirro = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("rinite alérgica(FC = 0.85) = False", "rinite alérgica(FC = 0.85) = True") for w in alfabeto_julgado] 
        #R8
        if "dor-de-cabeça = True" in alfabeto_julgado and "coriza = True" in alfabeto_julgado:
            alfabeto_julgado = [w.replace("sinusite(FC = 0.80) = False", "sinusite(FC = 0.80) = True") for w in alfabeto_julgado] 

        rodar = rodar + 1
    
    diagnosticos = ["covid19(FC = 0.80)", "gripe(FC = 0.90)", "mononucleose infecciosa(FC = 0.95)", "amigdalite(FC = 0.90)", "estresse(FC = 0.70)", "covid19(FC = 0.90)", "rinite alérgica(FC = 0.85)", "sinusite(FC = 0.80)"]

    aux = 0
    # Características
    for linha in verdadeiros:
        if aux == 0:
            print("\nVocê disse que tem os seguintes sintomas: \n")
            aux = aux + 1
        print("- " + linha + ";")

    aux = 0
    aux_2 = 0
    # Dizer diagnóstico
    for linha in diagnosticos:
        if linha + " = True" in alfabeto_julgado:
            if aux_2 == 0:
                print(f"\nPortanto, seu diagnóstico deve ser: {linha}", end="")
                aux_2 = aux_2 + 1
            else:
                print(f" ou {linha}", end="")
        else:
            aux = aux + 1
            continue

    if aux == 8:
        print("\nNenhum diagnóstico de encontrada.")

    print("")

if __name__ == "__main__":

    parar = False

    while parar == False:
        print("=== Diagnóstico ===")
                
        antecedentes = []
        descendentes = []
        antecedentes_e_descendentes = []
        alfabeto = []
        verdadeiros = []
        abc = ["fadiga", "dor-de-cabeça", "dores-no-corpo", 
                "dores-de-garganta", "tosse", "covid19(FC = 0.80)",
                "garganta-inflamada","gripe(FC = 0.90)",
                "cansaço" ,"mononucleose infecciosa(FC = 0.95)","amigdalite(FC = 0.90)",
                "estresse(FC = 0.70)", "pulsação-elevada", "baixo-nível-oxigênio", "perda-de-olfato", 
                "perda-de-paladar", "covid19(FC = 0.90)", "coriza", "espirro","rinite alérgica(FC = 0.85)", 
                "sinusite(FC = 0.80)"]

        perguntas = ["Você tem tido fadiga? [S, N] ",
                    "Você tem tido dor de cabeça? [S, N] ",
                    "Você tem tido dores no corpo? [S, N] ",
                    "Você tem tido dores de garganta? [S, N] ",
                    "Você tem tido tosse? [S, N] ",
                    "Você está com a garganta inflamada? [S, N] ",
                    "Você tem sentido cansaço? [S, N] ",
                    "Sua pulsação está elevada? [S, N] ",
                    "Seu nível de oxigênio está baixo? [S, N] ",
                    "Você tem sentido perda de olfato? [S, N] ",
                    "Você tem tido perda de paladar? [S, N] ",
                    "Você tem tido coriza? [S, N] ",
                    "Você tem espirrado? [S, N] "]

        print("\nSeus dados:\n")
        with open("./diagnostico/regras_diagnostico.csv", "r") as base:
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
    x = 0

    # Faz as perguntas
    while (x < 13):

        diagnostico_perguntas.faz_perguntas(perguntas, verdadeiros)
        x = x + 1

    # Julga as respostas
    verifica(antecedentes, verdadeiros, alfabeto)