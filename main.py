from personagens import *

def batalhas(p1, p2):
    rounds = 1
    print("⚔️ Bem-vindos ao Coliseu!")

    while p1.vida > 0 and p2.vida > 0:
        print(f"\n=== Round {rounds} ===")
        print()

        # Turno p1
        print(f'Turno de {p1.__class__.__name__}')
        perdeu_turno = False
        p1.atacar(p2)
        if hasattr(p1, "habilidade_especial"):
            if isinstance(p1, Arqueiro):
                if p1.flecha_congelante >= 8:
                    perdeu_turno = p1.habilidade_especial(p2)
            elif isinstance(p1, Guerreiro) and p1.furia >= 4:
                usar = input("Usar habilidade especial? (s/n): ")
                if usar.lower() == "s":
                    p1.habilidade_especial(p2)
            elif isinstance(p1, Mago) and p1.buff_vida >= 7:
                p1.habilidade_especial()

        if p2.vida <= 0:
            print(f'{p2.__class__.__name__} foi derrotado!')
            break

        # Turno p2 (se não perdeu)
        if not perdeu_turno:
            print(f'Turno de {p2.__class__.__name__}')
            p2.atacar(p1)
            if isinstance(p2, Mago) and p2.buff_vida >= 7:
                p2.habilidade_especial()
            elif isinstance(p2, Guerreiro) and p2.furia >= 4:
                p2.habilidade_especial(p1)

        if p1.vida <= 0:
            print(f'{p1.__class__.__name__} foi derrotado!')
            break

        rounds += 1



robin_hood = Arqueiro(100, 50, 100)
merlin = Mago(100, ataque={'Bola de Fogo': 40, 'Magia Arcaica': 20}, defesa=100)
kratos = Guerreiro(400, 40, 200)

batalhas(robin_hood, kratos)
