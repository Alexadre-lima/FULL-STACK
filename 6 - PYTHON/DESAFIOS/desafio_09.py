# Sistema simples de login
usuario_correto = "admim"
senha_correta = "12345678"

usuario = input("Digite o seu usuario: ")
senha = input("Digite a sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")