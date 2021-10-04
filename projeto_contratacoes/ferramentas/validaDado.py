# Importando uma função que muda cor de textos no terminal, criada em outro arquivo
from ferramentas.create_db import Vagas
from .utilidades import textoCor

"""
Módulo de funções para validação de alguns dados como Nomes, CPFs e Datas de nascimento.

NOTA: Todas as funções são parecidas e utilizam o mesmo princípio. 
Irei comentar detalhadamente apenas a primeira e, em caso de peculiaridades,
farei comentários isolados na respectiva função.
"""

def validaNome(mensagem='Nome: '):
    """
    Função que valida nomes de forma a verificar se todos
    os caracteres são letras e não outros tipos de dados.
    
    :param mensagem: recebe uma mensagem que aparece no input
    :return nome: retorna o nome em forma de str
    """
    # loop para permitir nova inserção após um erro
    while True:
        try:
            # checagem dos dados recebidos
            nome = str(input(mensagem)).split() # transformo a entrada em uma lista para poder checar nomes compostos
            # se a lista estiver vazia gera um erro logo de início
            if nome == []:
                raise KeyboardInterrupt
            else:
                # checar se cada item na lista é composto apenas por letras
                for i in nome:
                    if i.isalpha():
                        pass
                    else:
                        raise ValueError
            # retransformar a lista em string para o retorno
            nome = ' '.join(nome)
        # tratamento de erros    
        except ValueError:
            # emitir os avisos de erro na cor vermelha
            textoCor('Tipo de dado inválido. Tente novamente!', 31)
        except KeyboardInterrupt:
            textoCor('Informação obrigatória. Impossível prosseguir!', 31)
        except:
            textoCor('Erro desconhecido. Tente novamente!',31)
        else:
            # após passar por todos os filtros é retornado o nome em forma de string
            return nome

def validaCPF(mensagem='CPF (somente números): '):
    """
    Função que valida CPFs de forma a verificar se todos
    os caracteres são numéricos e se não contém outros 
    tipos de dados.
    Também verifica o tamanho do CPF inserido, são sendo possível
    validar CPFs maiores ou menores do que 11 números.
    
    :param mensagem: recebe uma mensagem que aparece no input
    :return cpf: retorna cpf em formato str
    """
    while True:
        try:
            cpf = str(input(mensagem))
            cpf = list(cpf.strip(''))
            if cpf == []:
                raise KeyboardInterrupt
            else:
                # checar se cada digito é um número  
                for i in cpf:
                    if i.isnumeric():
                        pass
                    else:
                        raise ValueError
            if len(cpf) > 11 or len(cpf) < 11:
                    raise Exception
            cpf = ''.join(cpf)
                                                
        except ValueError:
            textoCor('Tipo de dado inválido. Tente novamente!', 31)
        except KeyboardInterrupt:
            textoCor('Informação obrigatória. Impossível prosseguir!', 31)
        except Exception:
            textoCor('Tamanho inválido. Verifique o dado digitado!', 31)
        except:
            textoCor('Erro desconhecido. Tente novamente!')
        else:
            return cpf
    

def validaNascimento(mensagem='Data nasc. (DD/MM/AAAA): '):
    """
    Função que valida datas de forma a verificar se todos
    os caracteres, entre as '/' são numéricos e não outros tipos de dados.
    Também verifica se o dia, mês e ano estão dentro dos limites válidos.
    
    :param mensagem: recebe uma mensagem que aparece no input
    :return data: retorna data em formato str
    """
    # variável que facilita a mudança do ano atual
    anoAtual = 2021
    
    while True:
        try:
            data = str(input(mensagem))
            data = list(data.split('/'))
            if data == []:
                raise KeyboardInterrupt
            else:    
                for i in data:
                    if i.isnumeric():
                        pass
                    else:
                        raise ValueError
                # utilizo dos índices para verificar cada dado
                if int(data[0]) > 31:
                    raise Exception('Dia')
                if int(data[1]) > 12:
                    raise Exception('Mês')
                if int(data[2]) > anoAtual:
                    raise Exception('Ano')
            data = '/'.join(data)  
                                  
        except ValueError:
            textoCor('Tipo de dado inválido. Tente novamente!', 31)
        except KeyboardInterrupt:
            textoCor('Informação obrigatória. Impossível prosseguir!', 31)
        except Exception:
            textoCor('Conteúdo(s) - DIA, MÊS ou ANO - Inválido(s)! Verifique os dados digitados!', 31)
        except:
            textoCor('Erro desconhecido. Tente novamente!', 31)
        else:
            return data


def validaVaga(mensagem='Vaga: ',inserir=False,vagaNome=str):
    """
    Função que valida vagas de forma a verificar se a vaga
    existe na base de dados, sendo impossível adicionar um
    candidato relacionado a uma vaga inexistente.
    
    :param mensagem: recebe uma mensagem que aparece no input
    :return vaga: retorna vaga em formato str
    """
    while True:
        vaga = ''
        try:
            if inserir == False:
                vaga = str(input(mensagem))
                validar = Vagas.select()
                for row in validar:
                    if vaga == row.vaga or int(vaga) == row.id:
                        existe = True
                        return vaga
                    else:
                        existe = False
                if existe:
                    pass
                else:
                    raise Exception                        
            else:
                validar = Vagas.select()
                for row in validar:
                    if vagaNome == row.vaga:
                        return True
                    else:
                        return False

        except ValueError:
            textoCor('Tipo de dado inválido. Tente novamente!', 31)
        except KeyboardInterrupt:
            textoCor('Informação obrigatória. Impossível prosseguir!', 31)
        except Exception:
            textoCor('Vaga não encontrada!', 31)
        except:
            textoCor('Erro desconhecido. Tente novamente!')
        else:
            return vaga

