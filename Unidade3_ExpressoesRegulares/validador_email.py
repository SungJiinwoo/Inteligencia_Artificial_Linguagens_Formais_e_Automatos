import re

padrao_email = re.compile(
    r"^(?!\.)(?!.*\.\.)(?!.*\.@)"
    r"[A-Za-z0-9._+-]+@"
    r"(?:(?!-)[A-Za-z0-9-]+(?<!-)\.)+"
    r"[A-Za-z]{2,}$"
)


def motivo_invalido(email):
    if " " in email:
        return "contém espaço"

    if "@" not in email:
        return "não possui @"

    if email.count("@") > 1:
        return "possui mais de um @"

    usuario, dominio = email.split("@")

    if usuario == "":
        return "não possui usuário"

    if usuario.startswith("."):
        return "o usuário começa com ponto"

    if usuario.endswith("."):
        return "possui ponto imediatamente antes de @"

    if ".." in email:
        return "possui dois pontos consecutivos"

    if dominio == "":
        return "não possui domínio"

    if "." not in dominio:
        return "não possui extensão"

    partes_dominio = dominio.split(".")

    for parte in partes_dominio[:-1]:
        if parte.startswith("-") or parte.endswith("-"):
            return "há hífen no início ou no final de uma parte do domínio"

    extensao = partes_dominio[-1]

    if len(extensao) < 2 or not extensao.isalpha():
        return "a extensão é inválida"

    return "não corresponde ao padrão de e-mail"


validos = []
invalidos = []

for i in range(5):
    email = input(f"Digite o {i + 1}º endereço de e-mail: ")

    if padrao_email.fullmatch(email):
        validos.append(email)
    else:
        invalidos.append((email, motivo_invalido(email)))


print("\nE-mails válidos:")
for email in validos:
    print(email)


print("\nE-mails inválidos:")
for email, motivo in invalidos:
    print(f"{email} - {motivo}")
