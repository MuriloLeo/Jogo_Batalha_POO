from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Personagem(ABC):
    vida: int = 0
    ataque: int = 0
    defesa: int = 0

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
        

class Mago(Personagem):
    ataque: dict[str] = field(default_factory=list)
    buff_vida = 0

    def atacar(self):
        self.buff_vida += 5
        for magia, dmg in self.ataque.items:
            print(f'{magia}: {dmg}')
        magia_selecionada = str(input('Qual ataque deseja usar?: '))
        if magia_selecionada in self.ataque.keys():
            print(f'{magia_selecionada} Lançada: {[self.ataque.items[magia_selecionada]]} de dano')
            self.buff_vida += 1
                

    def habilidade_especial(self):
        if self.buff_vida >= 7:
            self.vida += self.buff_vida
            return f'Aumento de vida ativado! \n + {self.buff_vida} adicionado a vida! \n Vida atual: {self.vida}'
        else:
            return f'Aumento de vida acumulando...'

class Arqueiro(Personagem):
    ...


# murilo = Guerreiro(10, 20, 30)

# for ataque in range(0,5):
#     murilo.atacar()
#     print(murilo.furia)
#     print()
#     print(murilo.habilidade_especial())

murilo = Mago()