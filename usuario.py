# class Usuario:
#     def __init__(self, nome, apartamento, email):
#         self.nome = nome
#         self.apartamento = apartamento
#         self.email = email

class Usuario:
    def __init__(self, nome, apartamento, bloco, email, telefone):
        self.nome = nome
        self.apartamento = apartamento
        self.bloco = bloco
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome}, Apto: {self.apartamento}, Bloco: {self.bloco}, Email: {self.email}, Tel: {self.telefone}'