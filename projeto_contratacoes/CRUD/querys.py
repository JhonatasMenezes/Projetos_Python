from create_db import *

db.connect()
usuario = Candidatos.select()
print(usuario)
    