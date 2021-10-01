import datetime
from dateutil.relativedelta import relativedelta
from Modulos.utilidades import textoCor

"""
Módulo de funções para validação de alguns dados como Nomes, CPFs e Datas de nascimento.

NOTA: Todas as funções são parecidas e utilizam o mesmo princípio. 
Irei comentar detalhadamente apenas a primeira e, em caso de peculiaridades,
farei comentários subjetivos a sua respectiva função.
"""

def validaNome(mensagem='Nome: '):
    """
    Função que valida nomes de forma a verificar se todos
    os caracteres são letras e não outros tipos de dados.
    
    :param mensagem: recebe uma mensagem que aparece no input
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
            textoCor('Tipo de dado inválido. Tente novamente!', 31)
        except KeyboardInterrupt:
            textoCor('Informação obrigatória. Impossível prosseguir!', 31)
        except:
            textoCor('Erro desconhecido. Tente novamente!',31)
        else:
            # após passar por todos os filtros é retornado o nome em forma de string
            return nome

def validaCPF(mensagem='CPF: '):
    """
    Função que valida CPFs de forma a verificar se todos
    os caracteres são numéricos e se não contém outros 
    tipos de dados.
    Também verifica o tamanho do CPF inserido, são sendo possível
    validar CPFs maiores ou menores do que 11 números.
    
    :param mensagem: recebe uma mensagem que aparece no input
    """
    while True:
        try:
            cpf = str(input(mensagem))
            cpf = list(cpf.strip(''))
            if cpf == []:
                raise KeyboardInterrupt
            else:    
                for i in cpf:
                    if i.isnumeric():
                        pass
                    else:
                        raise ValueError
            if len(cpf) > 11 or len(cpf) < 11:
                    raise Exception('Tamanho inválido')
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
    """
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
                if int(data[0]) > 31:
                    raise Exception('Dia')
                if int(data[1]) > 12:
                    raise Exception('Mês')
                if int(data[2]) > 2021:
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


def idade(dataNasc:str):
    """
    Função que determina a idade em anos, à partir de uma data informada 
    no formato string.
    
    :param dataNasc: uma data no formato 'DD/MM/AAAA'
    """
    # dividir as informações em uma lista
    dataNasc = dataNasc.split('/')
    # transformar os dados em uma data
    data = datetime.date(int(dataNasc[2]),int(dataNasc[1]),int(dataNasc[0]))
    # pegar data atual
    atual = datetime.datetime.utcnow()
    atual = atual.date()
    # calcular diferença de anos entre as datas
    idade = relativedelta(atual, data)
    idade = idade.years
    return idade