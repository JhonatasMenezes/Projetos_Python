from create_db import Candidatos, Vagas
from ferramentas.utilidades import textoCor
from time import sleep

def inserir(*dado, tabela):
    if tabela == 'Vagas':
        try:
            tab = Vagas()
            tab.insert(dado).execute()
        except:
            textoCor('Erro! Tente Novamente.',31)
        else:
            tab.save()
            textoCor(f'Vaga {tab.vaga} salva com sucesso!',33)
            sleep(3)
            
    elif tabela == 'Candidato':
        try:
            tab = Candidatos()
            dados = []
            for cada in  dado:
                dados.append(cada)
            tab.insert_many(dados).execute()
        except:
            textoCor("Erro! Tente novamente.",31)
        else:
            tab.save()
            textoCor(f'Candidato {tab.nome} salvo com sucesso!',33)
            sleep(3)


def atualizar(id,campo,dado,tabela):
    dado = str(dado)
    if tabela == 'Vagas':
        try:
            tab = Vagas()
            tab.get(Vagas.id == id)
            tab.vaga = dado
        except:
            textoCor('Erro! Tente novamente.',31)
        else:
            tab.save()
            textoCor(f'Vaga {dado} adicionada com sucesso!',33)
            sleep(3)
    if tabela == 'Candidatos':
        try:
            tab = Candidatos()
            tab.get(Candidatos.id == id)       
            if campo == 'nome':
                tab.nome = dado
            elif campo == 'sobrenome':
                tab.sobrenome = dado
            elif campo == 'CPF':
                tab.CPF = dado
            elif campo == 'dataNascimento':
                tab.data_nascimento = dado
            elif campo == 'vaga':
                tab.vaga = dado
            else:
                raise Exception
        except Exception:
            textoCor(f'Campo "{campo}" não encontrado!',31)
        except:
            textoCor('Erro! Tente novamente.',31)
        else:
            tab.save()
            textoCor(f"Usuário {id} atualizado com sucesso!",33)
            sleep(3)
            
             
def deletar(id, tabela):
    if tabela == 'Vagas':
        try:
            tab = Vagas()
            tab.delete().where(Vagas.id == id)            
        except:
            textoCor('Erro! Tente Novamente.',31)
        else:
            tab.save()
            textoCor(f'Vaga "{id}" deletada com sucesso!',33)
            sleep(3)
            
    elif tabela == 'Candidato':
        try:
            tab = Candidatos()
            tab.delete().where(Candidatos.id == id)
        except:
            textoCor("Erro! Tente novamente.",31)
        else:
            tab.save()
            textoCor(f'Candidato {id} deletado com sucesso!',33)
            sleep(3)


