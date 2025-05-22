import json
import os

# Cadastro de pessoas - CÓDIGO COM ERROS DE SEGURANÇA, SINTAXE E SEMÂNTICA

USERS_FILE = "usuarios.json"

def carregar_usuarios()
    if not os.path.exists(USERS_FILE):  # ❌ ERRO DE SINTAXE: falta ':' na definição da função
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(USERS_FILE, "w") as f:
        json.dump(usuarios, f)

def cadastrar_usuario():
    print("=== Cadastro de Usuário ===")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")  # ❌ Armazena senha sem criptografia
    idade = input("Idade: ")

    idade = eval(idade)  # ❌ Perigoso e vulnerável

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "idade": idade
    }

    usuarios = carregar_usuarios()
    usuarios.append(novo_usuarios)  # ❌ ERRO SEMÂNTICO: variável 'novo_usuarios' não existe
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("=== Lista de Usuários ===")
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

def main():
    while True:
        print("\n1. Cadastrar usuário\n2. Listar usuários\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()