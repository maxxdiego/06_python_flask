from time import sleep

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano inválido! Saindo do sistema...')
            exit()
  
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            print(f'O cliente {self.nome} alterou o plano de {self.plano} para {novo_plano}!')
            sleep(2)
            self.plano = novo_plano
        else:
            print('Plano inválido!')
     
            
    def ver_filme(self, filme, plano_filme):
        print(f'O cliente {self.nome} escolheu o filme [ {filme} ]!')
        print()
        sleep(2)
        print(f'Tentando executar o filme...')
        sleep(2)
        if self.plano == plano_filme:
            print(f'Exibindo filme {filme}...')
            sleep(2)
            print('::..' * 20)
            sleep(2)
        elif self.plano == 'Premium':
            print(f'Exibindo filme {filme}...')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print(f'Não é possível executar o filme. Faça upgrade para Premium para ver esse filme.')
            sleep(2)
        else:
            print('Plano inválido!')
            
            
class Filme:
    def __init__(self, titulo, plano):
        self.titulo = titulo
        self.plano = plano
        
cliente = Cliente('Diego', 'diego@email.com', 'Basic')

filme = Filme('Titanic', 'Premium')

print(f'Atualmente o plano do cliente {cliente.nome} é [ {cliente.plano} ].')
cliente.ver_filme(filme.titulo, filme.plano)
print()

cliente.mudar_plano('Premium')

print()
cliente.ver_filme(filme.titulo, filme.plano)
