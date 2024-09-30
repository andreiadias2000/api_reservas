# Cadastrando as salas

SALAS = {
    'A': 'Salão de Festas',
    'B': 'Churrasqueira 1',
    'C': 'Churrasqueira 2',
    'D': 'Churrasqueira 3',
    'E': 'Churrasqueira 4'
}
# salao_de_festas = Sala("Salão de Festas")
# churrasqueira_1 = Sala("Churrasqueira 1")
# churrasqueira_2 = Sala("Churrasqueira 2")
# churrasqueira_3 = Sala("Churrasqueira 3")
# churrasqueira_4 = Sala("Churrasqueira 4")

# Lista de todas as salas
salas = [salao_de_festas, churrasqueira_1, churrasqueira_2, churrasqueira_3, churrasqueira_4]


class Sala:
    def __init__(self, nome):
        self.nome = nome
        self.reservas = {}

    def verificar_disponibilidade(self, data):
        return data not in self.reservas

    def reservar(self, data, usuario):
        if self.verificar_disponibilidade(data):
            self.reservas[data] = usuario
            print(f"Sala {self.nome} reservada com sucesso para {usuario.nome} em {data}")
        else:
            print(f"Sala {self.nome} já está reservada na data {data}")

    def cancelar_reserva(self, data, usuario):
        if data in self.reservas and self.reservas[data] == usuario:
            del self.reservas[data]
            print(f"Reserva de {usuario.nome} para a sala {self.nome} em {data} foi cancelada.")
        else:
            print(f"Não há reserva de {usuario.nome} para cancelar na data {data}.")
