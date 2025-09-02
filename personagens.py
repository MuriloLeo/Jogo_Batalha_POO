import random
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Personagem(ABC):
    vida: int = 0
    ataque: int = 0
    defesa: int = 0

    def __post_init__(self):
        if self.vida <= 0:
            raise ValueError("A vida deve ser maior que 0!")
        if not isinstance(self.ataque, int) or self.ataque <= 0:
            raise ValueError("O ataque deve ser maior que 0!")
        if self.defesa <= 0:
            raise ValueError("A defesa deve ser maior que 0!")

    @abstractmethod
    def atacar(self, alvo):
        ...

    @abstractmethod
    def habilidade_especial(self, alvo):
        ...


class Guerreiro(Personagem):
    furia = 0

    def atacar(self, alvo):
        self.furia += 1
        dano = max(0, self.ataque - alvo.defesa // 10)
        alvo.vida -= dano
        print(f'Ataque de espada causa {dano} de dano! (Fúria {self.furia}/4)')
        if self.furia >= 4:
            print(f'⚔️ Fúria acumulada! Habilidade especial pronta!')

    def habilidade_especial(self, alvo):
        if self.furia >= 4:
            self.furia = 0
            alvo.vida -= 10
            print(f'Fúria ativada! +10 de sangramento em {alvo.__class__.__name__}')
        else:
            print(f'Fúria ainda acumulando...')


@dataclass(repr=False)
class Mago(Personagem):
    ataque: dict[str, int] = field(default_factory=dict)
    buff_vida = 0

    def __repr__(self):
        return f"Mago(vida={self.vida}, magias={list(self.ataque.keys())}, defesa={self.defesa})"

    def __post_init__(self):
        if self.vida <= 0:
            raise ValueError("A vida deve ser maior que 0!")
        if self.defesa <= 0:
            raise ValueError("A defesa deve ser maior que 0!")
        if not self.ataque:
            raise ValueError("O mago precisa ter pelo menos uma magia!")
        if not all(isinstance(dano, int) and dano > 0 for dano in self.ataque.values()):
            raise ValueError("Todas as magias devem ter dano inteiro positivo!")

    def atacar(self, alvo):
        magia_selecionada = random.choice(list(self.ataque.keys()))
        dano = max(0, self.ataque[magia_selecionada] - alvo.defesa // 10)
        alvo.vida -= dano
        self.buff_vida += 1
        print(f'🪄 {magia_selecionada} causa {dano} de dano! (Buff Vida {self.buff_vida}/7)')

    def habilidade_especial(self, alvo=None):
        if self.buff_vida >= 7:
            self.vida += self.buff_vida
            print(f'Aumento de vida ativado! +{self.buff_vida} de vida (Total: {self.vida})')
            self.buff_vida = 0
        else:
            print(f'Aumento de vida acumulando...')



class Arqueiro(Personagem):
    flecha_congelante = 0

    def atacar(self, alvo):
        self.flecha_congelante += 1
        dano = max(0, self.ataque - alvo.defesa // 10)
        alvo.vida -= dano
        print(f'🏹 Flecha acerta {dano} de dano! (Runas {self.flecha_congelante}/8)')
        if self.flecha_congelante >= 8:
            print(f'❄️ Runa congelante pronta!')

    def habilidade_especial(self, alvo):
        if self.flecha_congelante >= 8:
            self.flecha_congelante = 0
            alvo.vida -= 15
            print(f'❄️ Flecha de gelo disparada! +15 de dano e inimigo perde turno!')
            return True 
        else:
            print(f'Runas ainda esfriando...')
            return False
