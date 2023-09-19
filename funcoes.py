import requests
from datetime import date, datetime, timedelta


def buscaMoedas():
    request = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json")

    moedas = request.json()

    moedas = moedas["value"]

    lista_moedas = []

    for i, moeda in enumerate(moedas):
        lista_moedas.append(moedas[i]["simbolo"])

    return lista_moedas

def buscaDados(moeda, data):
    try:
        dataSelecionada = datetime.strptime(data, '%d-%m-%Y')
        weekday = date.isoweekday(dataSelecionada)

        if weekday == 6 or weekday == 7:
            dataBusca = dataSelecionada - timedelta(weekday - 5)
            dataBusca = str(dataBusca)
            dataBusca = dataBusca.split(" ")
            dataBusca = dataBusca[0]
            year, month, day = (int(x) for x in dataBusca.split('-')) 
        else:
            dataBusca = datetime.strftime(dataSelecionada, '%d-%m-%Y')
            dataBusca = dataBusca.split(" ")
            dataBusca = dataBusca[0]
            day, month, year = (int(x) for x in dataBusca.split('-'))
        
        if month < 10:
            month = "0" + str(month)

        dataBusca = f"{month}-{day}-{year}"

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)?@codigoMoeda='{moeda}'&@dataInicialCotacao='{dataBusca}'&@dataFinalCotacao='{dataBusca}'&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim"

        dadosAPI = requests.get(url)

        conteudo = dadosAPI.json()

        return conteudo
    except:
        return "Por favor, verifique se as informações estão corretas."
    
def buscaValorCompra(moeda, data):
    try:            
        dadosCompra = buscaDados(moeda, data)

        valorCompra = dadosCompra["value"][0]["cotacaoCompra"]

        return f"R${valorCompra:.2f}"

    except:
        return "Por favor, verifique se as informações estão corretas."

def buscaValorVenda(moeda, data):
    try:
        dadosVenda = buscaDados(moeda, data)

        valorVenda = dadosVenda["value"][0]["cotacaoVenda"]

        return f"R${valorVenda:.2f}"
    
    except:
        return "Por favor, verifique se as informações estão corretas."

def buscaDataHoraCotacao(moeda, data):
    try:
        dadosInformacao = buscaDados(moeda, data)

        dataHoraCotacao = dadosInformacao["value"][0]["dataHoraCotacao"]

        dataCotacao = dataHoraCotacao.split(' ')[0]

        horaCotacao = dataHoraCotacao.split(' ')[1]
        horaCotacao = horaCotacao.split('.')[0]
        horaCotacao = f"{horaCotacao.split(':')[0]}:{horaCotacao.split(':')[1]}"

        dataHoraFormatado = f"{dataCotacao} as {horaCotacao}"

        return  dataHoraFormatado
    
    except:
        return "Por favor, verifique se as informações estão corretas."
    

