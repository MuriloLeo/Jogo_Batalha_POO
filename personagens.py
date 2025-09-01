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
    def atacar(self):
        ...

    @abstractmethod
    def habilidade_especial(self):
        ...


class Guerreiro(Personagem):
    furia = 0

    def atacar(self):
        self.furia += 1 
        print(f'Ataque de espada: {self.ataque} de dano! Sua habilidade especial está acumulando...')
        if self.furia >= 4:
            print(f'Fúria acumulada! habilidade especial pronta para ser utilizada')

    def habilidade_especial(self):
        if self.furia >= 4:
            self.furia = 0
            return f'Efeito de fúria ativado! \n + 10 de sangramento'
        else:
            return f'Fúria acumulando...'
        

@dataclass(repr=False)
class Mago(Personagem):
    ataque: dict[str, int] = field(default_factory=dict)
    buff_vida = 0

    def __repr__(self):
        magias = [(m, v) for m, v in self.ataque.items()]
        return f"{__class__.__name__}(vida={self.vida}, magias={magias}, defesa={self.defesa})"
    
    def __post_init__(self):
        if self.vida <= 0:
            raise ValueError("A vida deve ser maior que 0!")
        if self.defesa <= 0:
            raise ValueError("A defesa deve ser maior que 0!")
        if not self.ataque:
            raise ValueError("O mago precisa ter pelo menos uma magia!")
        if not all(isinstance(dano, int) and dano > 0 for dano in self.ataque.values()):
            raise ValueError("Todas as magias devem ter dano inteiro positivo!")

    def atacar(self):
        for magia, dmg in self.ataque.items():
            print(f'{magia}: {dmg}')
        magia_selecionada = str(input('Qual ataque deseja usar?: '))
        if magia_selecionada in self.ataque.keys():
            print(f'{magia_selecionada} lançada: {self.ataque[magia_selecionada]} de dano')
            self.buff_vida += 1
        else:
            print('Ataque desconhecido... perca de turno!')
                
    def habilidade_especial(self):
        if self.buff_vida >= 7:
            self.vida += self.buff_vida
            print(f'Aumento de vida ativado! \n + {self.buff_vida} adicionado a vida! \n Vida atual: {self.vida}')
            self.buff_vida = 0
        else:
            return f'Aumento de vida acumulando...'

class Arqueiro(Personagem):
    flecha_congelante = 0
    
    def atacar(self):
        self.flecha_congelante += 1 
        print(f'Flecha disparada: {self.ataque} de dano! Sua habilidade especial está acumulando...')
        if self.flecha_congelante >= 4:
            print(f'Runa congelante liberada! habilidade especial pronta para ser utilizada')
    
    def habilidade_especial(self):
        if self.flecha_congelante >= 8:
            self.flecha_congelante = 0
            return f'Flecha de gelo disparada!\nEfeito de congelamento aplicado! O inimigo perde um turno'
        else:
            return f'Runa esfriando...'

