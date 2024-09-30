from usuario import Usuario
from sala import Sala

class SistemaReserva:
    def __init__(self):
        self.usuarios = []
        self.salas = [Sala("Salão de Festa"), Sala("Churrasqueira 1"), Sala("Churrasqueira 2"), Sala("Churrasqueira 3"), Sala("Churrasqueira 4")]

    # def cadastrar_usuario(self, nome, apartamento, email):
    #     usuario = Usuario(nome, apartamento, email)
    #     self.usuarios.append(usuario)
    #     print(f"Usuário {nome} cadastrado com sucesso.")
    
    def cadastrar_usuario():
        nome = input("Nome: ")
        apto = input("Número do Apartamento: ")
        bloco = input("Bloco (A/B/C/D): ").upper()
        email = input("Email: ")
        telefone = input("Telefone (apenas números): ")

    if bloco not in ['A', 'B', 'C', 'D', 'E','F', 'G', 'H']:
        print("Erro: Bloco inválido!")
        return
    
    usuario = User(nome, apto, bloco, email, telefone)
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso.")

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, Apartamento: {usuario.apartamento}, Email: {usuario.email}")

    def listar_salas(self):
        for sala in self.salas:
            print(f"Sala: {sala.nome}")

    def reservar_sala(self, nome_sala, data, usuario):
        for sala in self.salas:
            if sala.nome == nome_sala:
                sala.reservar(data, usuario)
                return
        print(f"Sala {nome_sala} não encontrada.")

    def cancelar_reserva(self, nome_sala, data, usuario):
        for sala in self.salas:
            if sala.nome == nome_sala:
                sala.cancelar_reserva(data, usuario)
                return
        print(f"Sala {nome_sala} não encontrada.")
