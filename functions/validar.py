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
                "sinistro": "N,
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
            dados['ecliente'] = 'S'
        else: 
            dados['ecliente'] = 'N'
    else:
        dados['ecliente'] = 'N'

    #Verificando contratos
    if 'veiculos' in recebidos:
        adimplente_list = []
        sinistro_list = []
        if len(recebidos['veiculos']) >= 1:
            for veiculo in recebidos['veiculos']:

                #Verificando se o contrato está inadimplente
                if 'adimplente' in veiculo:
                    if veiculo['adimplente'] == 'S':
                        adimplente_list.append('S')
                    else:
                        adimplente_list.append('N')

                #Verificando se o veiculo tem sinistro
                if 'sinistro' in veiculo:
                    if veiculo['sinistro'] == 'S':
                        sinistro_list.append('S')
                    else:
                        sinistro_list.append('N')
        
            if 'N' in adimplente_list:
                dados['inadimplente'] = 'S'
            else:
                dados['inadimplente'] = 'N' 

            if 'N' in sinistro_list:
                dados['sinistro'] = 'S'
            else:
                dados['sinistro'] = 'N'

        else:
            #Cadastro invalido
            dados['ecliente'] = 'N'
    else:
        #dados invalidos
        dados['ecliente'] = 'N'

    return dados