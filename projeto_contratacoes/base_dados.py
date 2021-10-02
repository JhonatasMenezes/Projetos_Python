from enum import unique
from peewee import *

db = SqliteDatabase('contratacoes.db')

class BaseModel(Model):
    
    class Meta:
        database = db
        
class Candidatos(BaseModel):
    nome = CharField(unique=True)


class Vagas(BaseModel):
    pass
