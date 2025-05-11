from dataclasses import dataclass, field, asdict

@dataclass
class Comment:
    id: int 
    text: str = "texto" # define valor padrão
    replies: list[int] = field(default_factory=list) # define valores mutáveis, para que sejam alterados em sua própria instância

@dataclass(frozen=True)
class CommentImmutable:
    id: int 

@dataclass
class CommentPostInit:
    id: int

    def __post_init__(self):
        if self.id < 0:
            print("id negativo!")

if __name__ == '__main__':
    comentario = Comment(id=3)
    print("mostrando __repr__", comentario) # vem com __repr__
    print("mostrando id", comentario.id) # 
    print("mostrando text", comentario.text)
    print("mostrando replies", comentario.replies)
    print("convertendo p/ dict", asdict(comentario))

    com1 = Comment(id=1)
    com2 = Comment(id=2)
    print("mostrando __eq__", com1 == com2)

    com_immutable = CommentImmutable(id=1)
    try: com_immutable.id = 1
    except Exception as ex: print("classe imutável retorna", ex)

    print("usando __post_init__")
    com_post_init = CommentPostInit(id=-1)