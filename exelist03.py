names = ["João", "Maria", "Kleber", "Caio", "Sarah"]
salarys = [1350.20, 240.50, 30.00, 830.15, 50.00]
account = 0

print("LISTA DE CLIENTES - BANCO NACIONAL\n")

for name in names:
    print(
        f"Conta {account + 1} | Nome: {name} | Saldo: R$ {salarys[account]:.2f}")
    account += 1

"""
Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for 
correta e false caso o contrário. Logo após elabore um “mini-sistema” de checar a 
senha inserida, onde o usuário tem 3 tentativas de senha e caso esse número seja 
ultrapassado o programa é encerrado.
"""
password = "flamengo"
password_entered = input("Enter password: ")
def check_password(password_entered):
    if password_entered == password:
        print("Login successfully")
    else:
        print("Password incorrect: Try again")
        while
        