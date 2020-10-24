import json
import requests
from time import sleep

from bs4 import BeautifulSoup as BS


def main(url):
    """Esse é o método principal que a partir da página de resumo das leis do ano, busca os links de cada lei e faz a cópia
    :param url: url das leis do ano.
    """
    # faz requisição para URL
    data = []
    links_to_scrap = []  # cria array que irá armazenar todos os links para os atos/leis
    atos = []

    r_obj = requests.Session()
    sleep(1)
    fr_soup = r_obj.get(url)
    sleep(1)
    soup = BS(fr_soup.content, "lxml")
    sleep(1)

    # pega os dados da tabela de atos
    tabela_atos = soup.find("table", attrs={"class": "ms-listviewtable"})

    # itera sobre cada linha da tabela de atos
    rows = tabela_atos.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if not cols:  # ignore empty col
            continue
        row_text_vals = [ele.text.strip() for ele in cols if ele.text.strip()]  # pega os dados da linha
        data.append(row_text_vals)
        links = [ele.a for ele in cols if ele.a]  # busca por links na coluna daquela linha
        link = links[0].attrs['href'] if links else []
        links_to_scrap.append(link)  #adiciona novo link de ato/lei ao array
        # cria objeto json com os dados iniciais
        ato = {
            "nome": row_text_vals[1],
            "lei": row_text_vals[2],
            "data": row_text_vals[3],
            "resumo": row_text_vals[5],
            "url": 'https://legislacao.fazenda.sp.gov.br' + link
        }
        atos.append(ato)
    print('foram encontrados ' + str(len(atos)) + ' atos no link ' + url)

    for ato in atos:
        scrap_ato(ato)  # faz o scrap (cópia de dados) de leis de cada link encontrado
    return


def scrap_ato(ato):
    """Esse método faz a cópia de dados das leis.
    :param ato: objeto json que contém a URL da lei.
    """

    r_obj = requests.Session()
    sleep(1)
    fr_soup = r_obj.get(ato['url'])
    sleep(1)
    soup = BS(fr_soup.content, "lxml")
    sleep(1)

    lei = soup.find("div", attrs={"id": "areaComentario"})
    ato['completo'] = lei.get_text()

    file_name = '_'.join(ato["nome"].replace('.', '').strip().split(' ')) + '.json'
    with open('files/' + file_name, 'w', encoding='utf8') as f:
        json.dump(ato, f, indent=2, ensure_ascii=False)
    print('[' + ato["nome"] + '] copiado com sucesso!')
