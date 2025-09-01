from personagens import Arqueiro, Guerreiro, Mago

robin_hood = Arqueiro(100, 50, 100)
merlin = Mago(100, ataque={'Bola de Fogo': 100, 'Magia Arcaica': 20}, defesa=100)


def batalhas(*personagens):
    rounds = 1
    sair = False

    print(f'Bem vindos ao Coliseu! Temos {len(personagens)} guerreiros para batalhar!')
    print(f'Round {rounds}')
    while sair != True:
        ...
