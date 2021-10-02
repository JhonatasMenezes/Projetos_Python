from peewee import *

"""
Irei usar o ORM Peewee para interagir com um Banco de Dados bem 
simples e leve, o SQLite. O arquivo do BD estará presente no 
diretório do programa, dentro da pasta CRUD.
"""

# Nome do BD, caso não exista, será criado
db = SqliteDatabase('contratacoes.db')

# Classe que herda a classe Model do Peewee e vai definir qual BD iremos usar 
class BaseModel(Model):
    
    class Meta:
        database = db
        
# Criação das tabelas através de classes
class Vagas(BaseModel):
    # definição dos campos e suas características
    # NOTA: caso não seja inserido um campo PrimaryKey, o peewee 
    # faz isso automaticamente, com um campo chamado ID que 
    # possuirá AUTOINCREMENT por padrão
    vaga = CharField(max_length=30)


class Candidatos(BaseModel):
    nome = CharField(max_length=50)
    sobrenome = CharField(max_length=50)
    CPF = CharField(max_length=11,unique=True)
    data_nascimento =CharField(max_length=10)
    idade = IntegerField()
    vaga = ForeignKeyField(Vagas)


# Função que cria/conecta no BD e cria as 
# tables com a DDL informada na classe
def criarTabela():
    db.connect()
    db.create_tables(
        [
            Vagas,
            Candidatos
        ], safe=True
    )
    db.close()

criarTabela() 