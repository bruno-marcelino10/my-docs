#### -- Resumo - Classes e Métodos (POO) -- ####

class Carro:
    '''
    A classe é chamada de "módulo" ou "objeto". Ela é o fundamento principal do paradigma "POO", e com ela podemos
    organizar as tarefas de forma que:

    - certas funções criadas dentro da classe só funcionam em atributos dessa classe;
    - podemos importar classes de outros scripts para o "__main__", que realizará as operações de maneira ordenada.

    '''

    cor = "Prata" # atributo da classe que é inicializado como o mesmo para qualquer instância dessa classe.

    # __str__: define o que será mostrado quando printarmos o objeto
    def __str__(self):
        return(self.modelo + " 9021 // " + str(self.ano))

    # __init__: define os parâmetros que devem ser inseridos para criar uma instância dessa classe
    def __init__(self, modelo, ano):
        # Estes serão os atributos específicos para cada instância dessa classe.
        self.modelo = modelo
        self.ano = ano

    # Os "métodos" são funções que só se aplicam aos objetos desta classe
    def mudar_ano(self, ano_novo):
        self.ano = ano_novo # altera um atributo da classe
        print("Ano alterado! Ano novo =", ano_novo) # é interessante incluir prints para facilitar a correção de erros

    @classmethod # são métodos da classe, que não têm acesso a nenhuma instância, somente atributos da classe
    def mudar_cor(cls, cor_nova):
        cls.cor = cor_nova
        print("Cor alterada! Cor nova =", cor_nova)

    @staticmethod # são métodos normais criados dentro da classe, não possuem acesso a nenhum atributo ou instância
    def info_carro():
        print("É um veículo automotor de 4 rodas!")

    # GETTERS E SETTERS: pega um atributo (get) e o linka a uma função que o altera (setter) automaticamente
    # @property
    # def ano(self):
    #     return self._ano
    #
    # @ano.setter
    # def ano(self, ano_inserido):
    #     if type(ano_inserido) == type(int):
    #         self._ano = ano_inserido
    #     else:
    #         print("ano errado!")

carro = Carro("Focus", 2006) # Criando um objeto (instância) da classe Carro

print(carro) # retorna o que foi definido em __str__
print(carro.ano) # retorna um atributo do Carro
carro.mudar_ano(2001) # aplica um método ao Carro

carro.mudar_cor("azul") # aplicando método de classe
Carro.info_carro() # aplicando método estático

'''
HERANÇA: é o processo de se criar uma classe maior que contém métodos utilizados por outras classes "menores".

As classes menores podem "herdar" os métodos e atributos da primeira, e assim conter somente os métodos que são
específicos delas. 

Podemos chamar o método __init__ da classe maior utilizando super().__init__(atributos) nas classes menores.
'''