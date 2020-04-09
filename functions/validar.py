#Validar JSON recebido
def dados(recebidos={}):
    '''
    estrutura esperada do json
    {
        "cpf": "29622747817",
        "ecliente": "S",
        "veiculos": [
            {
                "placa": "EQS1423",
                "vigencia": "29/11/2020",
                "status_contrato": "ATIVO",
                "adimplente": "S",
                "valor_inadimplente": "0",
                "titulo": "",
                "vencimento": "",
                "valor": "",
                "barras": "",
            }
        ],
        "atualizado_em": "09/04/2020"
    }
    '''
    dados = {}
    #Validando dados do cliente
    if 'ecliente' in recebidos:
        if recebidos['ecliente'] == 'S':
            dados['ecliente'] = True
        else: 
            dados['ecliente'] = False
    else:
        dados['ecliente'] = False

    #Verificando contratos
    if 'veiculos' in recebidos:
        adimplente_list = []
        sinistro_list = []
        if len(recebidos['veiculos'] >= 1):
            for veiculo in recebidos['veiculos']:

                #Verificando se o contrato está inadimplente
                if 'adimplente' in recebidos['veiculos']['veiculo']:
                    if recebidos['veiculos']['veiculo']['adimplente'] == 'S':
                        adimplente_list.append('S')
                    else:
                        adimplente_list.append('N')

                #Verificando se o veiculo tem sinistro
                if 'sinistro' in recebidos['veiculos']['veiculo']:
                    if recebidos['veiculos']['veiculo']['sinistro'] == 'S':
                        sinistro_list.append('S')
                    else:
                        sinistro_list.append('N')
        
            if 'N' in adimplente_list:
                dados['inadimplente'] = True
            else:
                dados['inadimplente'] = False 

            if 'N' in sinistro_list:
                dados['sinistro'] = True
            else:
                dados['sinistro'] = False

        else:
            #Cadastro invalido
            dados['ecliente'] = False
    else:
        #dados invalidos
        dados['ecliente'] = False

    return dados