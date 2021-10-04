from .create_db import Candidatos, Vagas, db
from .utilidades import textoCor
from time import sleep

# Módulo criado para ajudar nas atividades junto ao Banco de Dados


def inserir(dado, tabela):
    """
    Função que serve para inserir dados no BD.
    Recebe um conjunto de dados e insere cada dado 
    mediante seu índice.
    
    :param dado: recebe dicionário ou lista de dicionários
    :param tabela: recebe str com o nome da tabela a ser inserida
    """
    if tabela == 'Vagas':
        try:
            tab = Vagas.create(vaga=dado)
            tab.save()
        except:
            textoCor('Erro! Tente Novamente.',31)
        else:
            textoCor(f'Vaga {dado} salva com sucesso!',32)
            sleep(3)
            
    elif tabela == 'Candidatos':
        try:
            if type(dado) == list:
                for cada in dado:
                    tab = Candidatos.create(nome=cada['nome'], sobrenome=cada['sobrenome'],
                                            CPF=cada['CPF'], data_nascimento=cada['dataNascimento'],
                                            idade=cada['idade'], vaga=cada['vaga'])
            else:
                tab = Candidatos.create(nome=dado['nome'], sobrenome=dado['sobrenome'],
                                        CPF=dado['CPF'], data_nascimento=dado['dataNascimento'],
                                        idade=dado['idade'], vaga=dado['vaga'])
            tab.save()
        except Exception as e:
            textoCor(e,31)
        except:
            textoCor("Erro! Tente novamente.",31)
        else:
            textoCor(f"{len(dado)} candidato(s) salvo com sucesso!",32)
            sleep(3)


def atualizar(id,campo,dado,tabela):
    """
    Função que atualiza dados emuma tabela do BD.
    
    :param id: recebe o id da linha a ser atualizada
    :param campo: recebe o campoa ser atualizado
    :param dado: o dado inserido
    :param tabela: a tabela a ser modificada
    """
    dado = str(dado)
    if tabela == 'Vagas':
        try:
            tab = Vagas.get(Vagas.id == id)
            tab.vaga = dado
            tab.save()
        except:
            textoCor('Erro! Tente novamente.',31)
        else:
            textoCor(f'Vaga {id} atualizada com sucesso!',32)
            sleep(3)
    if tabela == 'Candidatos':
        try:
            tab = Candidatos.get(Candidatos.id == id)       
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
            tab.save()
        except Exception:
            textoCor(f'Campo "{campo}" não encontrado!',31)
        except:
            textoCor('Erro! Tente novamente.',31)
        else:
            textoCor(f"Usuário {id} atualizado com sucesso!",32)
            sleep(3)
            
             
def deletar(id, tabela):
    """
    Função que deleta uma linha da tabela, 
    recebendo o Id como parâmetro.
    
    :param id: recebe int
    :param tabela: recebe str com nome da tabela
    """
    if tabela == 'Vagas':
        try:
            tab = Vagas.get(Vagas.id == id)            
            tab.delete_instance()
        except:
            textoCor('Erro! Tente Novamente.',31)
        else:
            textoCor(f'Vaga "{id}" deletada com sucesso!',32)
            sleep(3)
            
    elif tabela == 'Candidatos':
        try:
            tab = Candidatos.get(Candidatos.id == id)
            tab.delete_instance()
        except Exception as e:
            textoCor(e,31)
        except:
            textoCor("Erro! Tente novamente.",31)
        else:
            textoCor(f'Candidato {id} deletado com sucesso!',32)
            sleep(3)

