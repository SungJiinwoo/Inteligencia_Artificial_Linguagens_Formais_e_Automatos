"""Confere a máquina de 0ⁿ1ⁿ com todas as palavras de 0 e 1 até 10 símbolos.

Rodar: python testar_maquina.py
"""

from itertools import product

from maquina_turing import executar


def esperado(palavra):
    metade = len(palavra) // 2
    return len(palavra) > 0 and palavra == "0" * metade + "1" * metade


erros = 0
total = 0
for tamanho in range(0, 11):
    for simbolos in product("01", repeat=tamanho):
        palavra = "".join(simbolos)
        resultado, _ = executar(palavra, mostrar=False)
        total += 1
        if (resultado == "ACEITA") != esperado(palavra):
            erros += 1
            print("ERRO:", repr(palavra), resultado)

print(f"{total} palavras testadas, {erros} erro(s)")
