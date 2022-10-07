class Pessoa:
    def __init__(self,nome, idade):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__== '__main__' :
    p = Pessoa('Pedro',20)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
