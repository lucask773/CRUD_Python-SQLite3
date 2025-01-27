import sqlite3 #importando modulo

conectar = sqlite3.connect("Cliente.db")
cursor = conectar.cursor()

# Criando tabela Clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT UNIQUE NOT NULL,
    endereco TEXT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP      
)
""" 
)
conectar.commit() # Confirmando comando

# Criando funções CRUD

def criar_cliente(nome, email, telefone, endereco):
    try:
        cursor.execute("""
        INSERT INTO Clientes (nome, email, telefone, endereco)
        VALUES (?, ?, ?, ?)""", (nome, email, telefone, endereco))
        conectar.commit()
        print('Cliente foi cadastrado com sucesso!')
    except sqlite3.IntegrityError:
        print('Este cadastro já foi feito')

# Consultando tabela Clientes

def listar_clientes():
    cursor.execute("SELECT * FROM Clientes")
    Clientes = cursor.fetchall() # Retorna consulta
    for cliente in Clientes:
        print(cliente)

# Atualizando tabela Clientes

def atualizar_cliente(id_cliente, nome, email, telefone, endereco):
    cursor.execute(""" 
    UPDATE Clientes
    SET nome = ?, email = ?, telefone = ?, endereco = ?
    WHERE id = ?""", (nome, email, telefone, endereco, id_cliente))
    conectar.commit()
    print("Cliente atualizado com sucesso!")

# Deletando indice da tabela cliente

def deletar_cliente(id_cliente):
    cursor.execute(" DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conectar.commit()

# Menu para interação Cadastro cliente

while True:

    print("MENU")
    print("1. Cadastrar cliente")
    print("2. Consultar clientes")
    print("3. Atualizar cliente")
    print("4. Deletar cliente")
    print("5. Sair")

    escolha = input('Digite o numero da opção escolhida:')

# Determinando 

    # Cadastrando clientes na tabela
    if escolha == '1':
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        criar_cliente(nome, email, telefone, endereco)
    
    # Listando clientes na tabela
    elif escolha == '2':
        listar_clientes()
    
    # Atualizando clientes na tabela
    elif escolha == '3':
        id_cliente = int(input("ID do cliente: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")
        endereco = input("Novo endereço: ")
        atualizar_cliente(id_cliente, nome, email, telefone, endereco)

    # Deletando cliente da tabela
    elif escolha == '4':
        id_cliente = int(input("ID do cliente "))
        deletar_cliente(id_cliente)
    
    # Sair do programa
    elif escolha == "5":
        print("Saindo...")
        conectar.close()
        break

    # Opção invalida

    else:
        print("Opção invalida.")

