from sistema_reserva import SistemaReserva
import datetime
from usuario import Usuario
from reservation import Reservation

def menu():
    print("\n--- Sistema de Reservas ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Listar Salas")
    print("4. Reservar Sala")
    print("5. Cancelar Reserva")
    print("0. Sair")

def main():
    sistema = SistemaReserva()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do usuário: ")
            apartamento = input("Número do apartamento: ")
            email = input("Email: ")
            sistema.cadastrar_usuario(nome, apartamento, email)

        elif opcao == '2':
            sistema.listar_usuarios()

        elif opcao == '3':
            sistema.listar_salas()

        elif opcao == '4':
            nome_sala = input("Nome da sala (Salão de Festa ou Churrasqueira 1 a 4): ")
            data = input("Data da reserva (dd/mm/aaaa): ")
            nome_usuario = input("Nome do usuário que está fazendo a reserva: ")
            usuario = next((u for u in sistema.usuarios if u.nome == nome_usuario), None)
            if usuario:
                sistema.reservar_sala(nome_sala, data, usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == '5':
            nome_sala = input("Nome da sala (Salão de Festa ou Churrasqueira 1 a 4): ")
            data = input("Data da reserva (dd/mm/aaaa): ")
            nome_usuario = input("Nome do usuário que está cancelando a reserva: ")
            usuario = next((u for u in sistema.usuarios if u.nome == nome_usuario), None)
            if usuario:
                sistema.cancelar_reserva(nome_sala, data, usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
