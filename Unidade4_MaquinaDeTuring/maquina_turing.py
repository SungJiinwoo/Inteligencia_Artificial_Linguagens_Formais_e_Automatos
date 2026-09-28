"""Máquina de Turing que reconhece 0ⁿ1ⁿ (n >= 1).

Ideia: a cada volta marca o 0 mais à esquerda com X e o 1 mais à esquerda
com Y. Se no fim sobrar só X e Y, aceita.

Rodar: python maquina_turing.py 0011 000111 00111
"""

import sys

BRANCO = "_"

# (estado, símbolo lido) -> (símbolo escrito, movimento, próximo estado)
transicoes = {
    ("q0", "0"): ("X", "D", "q1"),
    ("q0", "Y"): ("Y", "D", "q3"),

    ("q1", "0"): ("0", "D", "q1"),
    ("q1", "Y"): ("Y", "D", "q1"),
    ("q1", "1"): ("Y", "E", "q2"),

    ("q2", "0"): ("0", "E", "q2"),
    ("q2", "Y"): ("Y", "E", "q2"),
    ("q2", "X"): ("X", "D", "q0"),

    ("q3", "Y"): ("Y", "D", "q3"),
    ("q3", BRANCO): (BRANCO, "D", "qaceita"),
}


def mostrar_fita(fita, cabeca):
    celulas = ""
    for i, simbolo in enumerate(fita):
        celulas += f"[{simbolo}]" if i == cabeca else f" {simbolo} "
    return celulas


def executar(palavra, mostrar=True):
    fita = list(palavra) + [BRANCO]
    cabeca = 0
    estado = "q0"
    estados = [estado]
    passo = 0

    while estado != "qaceita":
        if cabeca == len(fita):
            fita.append(BRANCO)
        lido = fita[cabeca]

        if mostrar:
            print(f"{passo:>3}  {estado:<7} {mostrar_fita(fita, cabeca)}")

        if (estado, lido) not in transicoes:
            # não existe regra para essa situação: a máquina para e rejeita
            return "REJEITA", estados

        escrito, movimento, estado = transicoes[(estado, lido)]
        fita[cabeca] = escrito
        cabeca += 1 if movimento == "D" else -1
        estados.append(estado)
        passo += 1

    if mostrar:
        print(f"{passo:>3}  {estado:<7} {mostrar_fita(fita, cabeca)}")
    return "ACEITA", estados


def resumir(estados):
    # junta estados repetidos seguidos: q1 q1 q1 vira q1
    resumo = [estados[0]]
    for e in estados[1:]:
        if e != resumo[-1]:
            resumo.append(e)
    return " → ".join(resumo)


if __name__ == "__main__":
    entradas = sys.argv[1:] or ["0011", "000111", "00111"]

    for palavra in entradas:
        print(f"\nEntrada: {palavra}")
        print("passo estado  fita")
        resultado, estados = executar(palavra)
        print(f"Resultado: {resultado}")
        print(f"Estados: {resumir(estados)}")
