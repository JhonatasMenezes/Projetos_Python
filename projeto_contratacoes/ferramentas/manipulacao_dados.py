from copy import Error
from peewee import IntegrityError
from .create_db import Candidatos, Vagas, db
from .utilidades import textoCor
from time import sleep

# Módulo criado para ajudar nas atividades junto ao Banco de Dados
# mesmo não sendo necessária a implementação das funções 'Atualizar' 
# e 'Deletar', me propus fazê-las para ganhar experiência no processo
# de interação com o BD.

# Valores que podem ser definidos mais facilmente dependendo do cenário
maxVagas = 5
candidatosPorVaga = 3

def inserir(dado, tabela):
    """
    Função que serve para inserir dados no BD.
    Recebe um conjunto de dados e insere cada dado 
    mediante seu índice.
    
    :param dado: recebe dicionário ou lista de dicionários
    :param tabela: recebe str com o nome da tabela a ser inserida
    """
    # inserção na tabela Vagas
    if tabela == 'Vagas':
        try:
            numVagas = Vagas.select()
            cont = 0
            for linha in numVagas:
                cont += 1
            if cont >= maxVagas:
                raise Exception
            tab = Vagas.create(vaga=dado)
            tab.save()
        except Exception:
            textoCor('Número máximo de vagas ja cadasradas!', 31)
            sleep(3)
        except:
            textoCor('Erro! Tente Novamente.',31)
            sleep(3)
        else:
            textoCor(f'Vaga {dado} salva com sucesso!',32)
            sleep(3)
     
    # inserção na tabela Candidatos        
    elif tabela == 'Candidatos':
        try:
            if type(dado) == list:
                naoCadastrado = []
                totalNaoCadastrado = 0
                # no momento da inserção, irá analisar se a vaga já possúi o n° máximo de candidatos
                for cada in dado:
                    numCandidatosVaga = Candidatos.select().where(Candidatos.vaga==cada['vaga'])
                    candidatosCadastrados = 0
                    for row in numCandidatosVaga:
                        candidatosCadastrados += 1
                    if candidatosCadastrados <= (candidatosPorVaga-1):
                        tab = Candidatos.create(nome=cada['nome'], sobrenome=cada['sobrenome'],
                                                CPF=cada['CPF'], data_nascimento=cada['dataNascimento'],
                                                idade=cada['idade'], maior=cada['maior'], vaga=cada['vaga'])
                    else:
                        # no caso de inserir mais de 1 candidato, o programa permite adicionar
                        # os candidatos que estão aptos de acordo com o n° de candidatos por vaga
                        # e não adiciona os que não estão aptos
                        naoCadastrado.append(cada)
                        totalNaoCadastrado += 1
                        pass  
                resp = len(dado) - totalNaoCadastrado
            else:
                numCandidatosVaga = Candidatos.select().where(Candidatos.vaga==dado['vaga'])
                candidatosCadastrados = 0
                for row in numCandidatosVaga:
                    candidatosCadastrados += 1
                if candidatosCadastrados <= (candidatosPorVaga-1):
                    tab = Candidatos.create(nome=dado['nome'], sobrenome=dado['sobrenome'],
                                            CPF=dado['CPF'], data_nascimento=dado['dataNascimento'],
                                            idade=dado['idade'], maior=dado['maior'], vaga=dado['vaga'])
                    resp = 1
                    tab.save()
                else:
                    raise Error
        except Error:
            textoCor('Máximo de 3 candidatos já registrados para essa vaga!',31)
            sleep(3)
        except IntegrityError:
            textoCor('CPF já registrado!',31)
            textoCor('Candidato não inserido!',31)
            sleep(3)
        except Exception as e:
            textoCor(e,31)
            textoCor('Candidato não inserido!',31)
            sleep(3)
        except:
            textoCor("Erro! Tente novamente.",31)
        else:
            # no caso de candidatos com vagas ja preenchidas, será retornada essa mensagem
            if len(naoCadastrado) > 0:
                for cada in range(0, len(naoCadastrado)):
                    textoCor(f"O candidato {naoCadastrado[cada]['nome']} não pode ser cadastrado.",31)
                    textoCor('Motivo: Número de candidatos por vaga excedido!',31)
            textoCor(f"{resp} candidato(s) salvo com sucesso!",32)
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
